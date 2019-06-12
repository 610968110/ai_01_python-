# -------------------------- 字符串 --------------------------
print("-" * 25, "字符串", "-" * 25)
letter = "Abcdea"
print(letter)
print(letter.count("A"))  # A出现的次数
print(letter.index("b"))  # b出现的pos  index1 = letter.index("f")  # 找不到会报错  rindex从结尾开始查找
# -------------------------- 去除空白 --------------------------
print("-" * 25, "去除空白", "-" * 25)
print("是否只包含空格(包括回车换行制表符等)", letter.isspace())
print("去除左右边空白", letter.strip())
print("去除左边空白", letter.lstrip())
print("去除右边空白", letter.rstrip())
# -------------------------- 数字判断，但是不能判断小数,三个从上到下越来越强大 --------------------------
print("-" * 25, "数字判断，但是不能判断小数,三个从上到下越来越强大", "-" * 25)
print("是否只包含十进制字符", "10".isdecimal())
print("是否只包含数字,全角数字、①、\u00b2", "①".isdigit())
print("是否只包含数字,全角数字、汉字数字", "五万一千四百八十二".isnumeric())
# -------------------------- 查找和替换 --------------------------
print("-" * 25, "查找和替换", "-" * 25)
print("abc".startswith("a"))
print("abc".endswith("c"))
print("abc".find("a"))  # 找不到返回-1  rfind从结尾开始查找
print("abc".replace("a", "A"))  # 没有不报错
# -------------------------- 文本对齐 --------------------------
print("-" * 25, "文本对齐", "-" * 25)
shi = ["a", "ab", "abc", "abcd"]
for s in shi:
    print(s.center(10, " "))  # 每行长度都是10，用" "填充,  rjust右对齐， ljust左对齐
# -------------------------- 拆分和连接 --------------------------
print("-" * 25, "拆分和连接", "-" * 25)
shi1 = "a\nb\nc "
split = shi1.split()
print(split)
print("~".join(split))  # 将split等返回的列表去掉[]等，改用~隔开
print(shi1.splitlines())  # 按照\n \r \r\n拆分
# -------------------------- 切片取中间 --------------------------
print("-" * 25, "切片取中间", "-" * 25)
shi2 = "0123456789"
print(shi2[1:2])  # 半开区间，包括前不包括后
print(shi2[1:])  # 到末尾
print(shi2[:])  # 完整的
print(shi2[::2])  # 隔一个输出，02468，第一个:代表完整字符串，第二个:代表步长  0 1 2 中间跨了两步
print(shi2[-1])  # 倒数第一个字符
print(shi2[-2:])  # 倒数两个字符
print(shi2[-1::-1])  # 逆序， 9~0，步长-1表示从右向左切,  或者shi2[::-1]
# -------------------------- 其他 --------------------------
print("-" * 25, "其他", "-" * 25)
print("abc".capitalize())  # 第一个字符转换为大写
print("a".upper())
print("A".lower())
print("Ab".swapcase())  # 大写变小写，小写变大写
print("123".zfill(4))  # 设置长度，前面用0填充

# print("至少包含一个字母，并且都是小写", letter.islower())  # 没有字母会报错
# print("至少包含一个字母，并且都是大写", letter.isupper())  # 没有字母会报错

# strip([chars])  # 在字符串上执行 lstrip()和 rstrip()
# expandtabs(tabsize=8)  # 把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8 。

# 4	bytes.decode(encoding=”utf-8”, errors=”strict”) Python3 中没有 decode 方法，但我们可以使用 bytes 对象的 decode() 方法来解码给定的 bytes 对象，这个 bytes 对象可以由 str.encode() 来编码返回。
# 5	encode(encoding=’UTF-8’,errors=’strict’) 以 encoding 指定的编码格式编码字符串，如果出错默认报一个ValueError 的异常，除非 errors 指定的是’ignore’或者’replace’
# 23 maketrans() 创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。
# 37 translate(table, deletechars=”“) 根据 str 给出的表(包含 256 个字符)转换 string 的字符, 要过滤掉的字符放到 deletechars 参数中
