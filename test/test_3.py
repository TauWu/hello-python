f = [{
    "name":{"firstname":"mike", "lastname":"top"},
    "ages":[12.12, 23]
}, {
    "name":{"firstname":"tom", "lastname":"top"},
    "ages":[12.12, 2]
}]

g = [{
    "name":{"firstname":"tim", "lastname":"top"},
    "ages":[12.12, 23]
}, {
    "name":{"firstname":"kick", "lastname":"top"},
    "ages":[12.12, 2]
}]

# 函数的定义，其中 var 是局部的一个变量名
def get_info(var):
    # for 是遍历列表的一个关键字
    for data in var:
        # 判断内容是否是 tom == 左右相等的意思 != 左右不等的意思
        if data["name"]["firstname"] != "tom":
            print(data)
        else:
            print("tom.......")

def get_info_2(var1):
    idx = 0
    while True:
        if idx > len(var1) - 1:
            break
        data = var1[idx]
        idx += 1
        print(data)

# 告诉Python解释器从哪里开始执行代码
if __name__ == "__main__":
    # 执行指定的函数，把f作为参数传给 get_info 函数
    get_info(f)
    get_info(g)
    get_info_2(f)
    get_info_2(g)
