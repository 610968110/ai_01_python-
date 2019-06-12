# -------------------------- 列表 --------------------------
print("-" * 25, "列表", "-" * 25)
list_name = ["a", "b", "c"]
print(list_name)  # 打印
print(list_name[0])  # 取值
print(len(list_name))  # 大小
list_name[0] = "A"  # 重新赋值
print(list_name)
list_name.append("d")  # 添加
print(list_name)
list_name.remove("d")  # 删除第一个出现的数据
print(list_name)
index = list_name.index("c")  # 查询位置
print(index)
list_name.insert(0, "z")  # 插入
list_name.pop()  # 删除末尾数据
print(list_name)
list_name.pop(0)  # 删除第一个数据
print(list_name)
list_name.extend(list_name)  # 添加一个列表  相当于+=
print(list_name)
list_name.sort()  # 排序
print(list_name)
list_name.sort(reverse=True)  # 逆序排序
print(list_name)
list_name.reverse()  # 逆序
print(list_name)
count = list_name.count("A")  # A出线侧次数
print(count)
del list_name[0]  # 删除第一个,是从内存中删除
print(list_name)

# -------------------------- 元祖 --------------------------
print("-" * 25, "元祖", "-" * 25)
# 元祖 定义完不能修改

_tuple = ("A", "B", 1, True)
_tuple1 = ("C",)  # 单元素加个，才是元祖，否则是str
print(_tuple)
print("%s的身高是%.2f，他的年龄是%d岁" % ("小明", 1.75, 18))  # 元祖可以用来格式化字符串

a = 1
b = 2
a, b = b, a
print("交换a和b的值 a=%d b=%d" % (a, b))

# -------------------------- 字典 --------------------------
print("-" * 25, "字典", "-" * 25)
map_user = {1: "小明",
            2: "大明"}
print(map_user.keys())  # key的元祖
print(map_user.values())  # value的元祖
print(map_user.items())  # （key,value）的元祖
print(map_user[2])  # 取值
# print(map_user[3])  # 取值不存在时会报错
map_user[3] = "大大明"
print(map_user)
map_user.pop(3)  # 删除
# map_user.pop(400)  # 删除不存在的会报错
print(map_user)
map_user1 = {0: "中明"}
map_user.update(map_user1)  # 合并两个字典
print(map_user)
# -------------------------- 其他生成方式 --------------------------
print("-" * 25, "其他生成方式", "-" * 25)
list_name = [i for i in range(10)]  # py2的xrange和py3的range是一样的，保存的是生成方式，而不是生成后的值
print(list_name)
