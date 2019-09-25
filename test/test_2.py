a = 1
# 将数字1赋值给变量a

b = "abc"
# 将字符串赋值给变量b
print(a, b)

c = [1,2,3,4,5,6,7]
print(c, c[0], c[1], c[2:5])
# c[0] 取索引为0的值
# c[2:5] 取2—5的切片

d = {
    "name":"mike",
    "age":12,
}
print(d, d["name"], d["age"])

e = {
    "name":{"firstname":"mike", "lastname":"top"},
    "ages":[12.12, 23]
}
print(e, e["name"]["firstname"], e["ages"][1])

f = [{
    "name":{"firstname":"mike", "lastname":"top"},
    "ages":[12.12, 23]
}, {
    "name":{"firstname":"tom", "lastname":"top"},
    "ages":[12.12, 2]
}]

print(f[0]["name"]["firstname"])
