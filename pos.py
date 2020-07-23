def group(prods: list):
    # todo: 对prods中的商品进行合并，汇总数量
    pass


def filter_num(num, prods):
    # todo: 对prods数量进行过滤，过滤出大于num的商品及其数量
    pass


# 在需要的情况下可以对模板的代码进行修改
if __name__ == "__main__":
    prods = [
        'ITEM000001',
        'ITEM000001',
        'ITEM000001',
        'ITEM000001',
        'ITEM000001',
        'ITEM000003-2',
        'ITEM000005',
        'ITEM000005',
        'ITEM000005'
    ]

    result = group(prods)
    for i in result:
        print(i[0], i[1])
    # output:
    # ITEM000001 5
    # ITEM000003 2
    # ITEM000005 3

    filtered = filter_num(2, result)
    for i in filtered:
        print(i[0], i[1])
    # output:
    # ITEM000001 5
    # ITEM000005 3




