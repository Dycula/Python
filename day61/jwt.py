import base64
import copy
import json
import time
import hmac


class Jwt():
    def __init__(self):
        pass

    @staticmethod
    def encode(payload, key, exp=500):
        header = {"typ": "JWT", "alg": "HS256"}

        # separators--指定序列化后的json串格式,第一个参数值每个键值对之间的连接符号,第二个参数值得是每一个键值对中键和值之间的连接符号
        # sort_keys---将序列化后的字符串进行排序
        header_json = json.dumps(header, separators=(",", ":"), sort_keys=True)
        header_bs = Jwt.b64encode(header_json.encode())

        # 参数中的payload{"username":"xxx"}
        payload = copy.deepcopy(payload)
        # 添加公有声明－－exp且值为未来时间戳
        payload["exp"] = int(time.time()) + exp
        payload_json = json.dumps(payload, separators=(",", ":"), sort_keys=True)
        payload_bs = Jwt.b64encode(payload_json.encode())

        # 签名
        if isinstance(key, str):
            key = key.encode()
        hm = hmac.new(key, header_bs + b"." + payload_bs, digestmod="SHA256")
        hm_bs = Jwt.b64encode(hm.digest())
        return header_bs + b"." + payload_bs + b"." + hm_bs

    @staticmethod
    def b64encode(j_s):
        # 替换生成出来的b64串中的占位符=
        return base64.urlsafe_b64encode(j_s).replace(b"=", b"")

    @staticmethod
    def b64decode(b64_s):
        rem = len(b64_s) % 4
        if rem > 0:
            b64_s += b"=" * (4 - rem)
        return base64.urlsafe_b64decode(b64_s)

    @staticmethod
    def decode(token, key):
        # 校验俩次签名结果
        # 检查exp公有声明
        # 注意b64=要补全
        # 校验成功　返回payload字典对象,失败的话raise
        header_b, payload_b, sign = token.split(b".")
        if isinstance(key, str):
            key = key.encode()
        # 比较俩次哈希结果
        hm = hmac.new(key, header_b + b"." + payload_b, digestmod="SHA256")
        if sign != Jwt.b64encode(hm.digest()):
            raise JwtSignError("俩次哈希结果不一样(sign error)")
        payload_json = Jwt.b64decode(payload_b)
        payload = json.loads(payload_json)
        # 校验exp是否过期
        exp = payload["exp"]
        now = time.time()
        if now > exp:
            raise JwtExpireError("过期(the token is exprie)")
        return payload


class JwtSignError(Exception):
    def __init__(self, error_msg):
        self.error_msg = error_msg

    def __str__(self):
        return "<JwtSignError is %s>" % self.error_msg

class JwtExpireError(Exception):
    def __init__(self, error_msg):
        self.error_msg = error_msg

    def __str__(self):
        return "<JwtExpireError is %s>" % self.error_msg

if __name__ == "__main__":
    s = Jwt.encode({"username": "hello"}, "abcdef")
    print(s)
    r=Jwt.decode(s,"abcdef")
    print(r)
