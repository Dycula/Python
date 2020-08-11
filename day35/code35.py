import getpass  # 隐藏输入
import hashlib  # 转换加密

# 输入隐藏
pwd = getpass.getpass("pw:")
print(pwd)

#算法加盐
hash = hashlib.md5("*#$%7a".encode())
# hash对象
#hash = hashlib.md5()  # 生成对象
hash.update(pwd.encode())  # 算法加密
pwd = hash.hexdigest()  # 提取加密后的密码
print(pwd)
