dict_commodity = {
    101: {"name": "屠龙刀", "price": 10000},
    102: {"name": "倚天剑", "price": 10000},
    103: {"name": "九阴白骨爪", "price": 8000},
    104: {"name": "九阳神功", "price": 9000},
    105: {"name": "降龙十八掌", "price": 8000},
    106: {"name": "乾坤大挪移", "price": 10000}
}

list_order= []
def gou_wu():
    """
        购物
    :return:
    """
    while True:

        item = input("1键购买，2键结算。")

        if item == "1":
            buying()
        elif item == "2":
            settlement()


def buying():
    print_commodity()
    dict_order= create_order()
    list_order.append(dict_order)
    print("添加到购物车。")


def create_order():
    while True:
        cid = int(input("请输入商品编号："))
        if cid in dict_commodity:
            break
        else:
            print("该商品不存在")
    count = int(input("请输入购买数量："))
    return {"cid": cid, "count": count}


def print_commodity():
    for key, value in dict_commodity.items():
        print("编号：%d，名称：%s，单价：%d。" % (key, value["name"], value["price"]))


def settlement():
    zong_jia = 0
    for item in list_order:
        commodity = dict_commodity[item["cid"]]
        print("商品：%s，单价：%d,数量:%d." % (commodity["name"], commodity["price"], item["count"]))
        zong_jia += commodity["price"] * item["count"]
    while True:
        money = float(input("总价%d元，请输入金额：" % zong_jia))
        if money >= zong_jia:
            print("购买成功，找回：%d元。" % (money - zong_jia))
            list_order.clear()
            break
        else:
            print("金额不足.")


gou_wu()