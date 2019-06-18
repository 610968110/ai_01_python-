import re


# py中的正则match函数默认会从头匹配，相当于加了^

def main():
    result = re.match(r"hello", "hello world")
    print(result)  # 如果不是NONE，则找到了匹配结果

    # -------------------------- 匹配单个字符 --------------------------
    print("-" * 25, "匹配单个字符", "-" * 25)
    # .  匹配任意一个字符，除了\n
    # [] 匹配[]中列举的字符  如[1234]、[1-4a-d]、[1-46-8] 这个不是46，是1-4、6-8
    # \d 匹配数字0-9
    # \D 匹配非数字
    # \s 匹配空白
    # \S 匹配非空白
    # \w 匹配单词字符，a-z  A-Z  0-9  _ 中文
    # \W 匹配非单词字符
    result = re.match(r".*",
                      """速度
                         与
                         激情
                      """,
                      re.S)  # 让.可以匹配\n
    print("让.可以匹配\\n", result.group())

    result = re.match(r"速度与激情\d", "速度与激情5")
    print("匹配0-9任意数字", result.group())

    result = re.match(r"速度与激情[1-4]", "速度与激情5")  # 等价于[1234]
    print("只匹配1234", result)

    # -------------------------- 匹配多个字符 --------------------------
    print("-" * 25, "匹配多个字符", "-" * 25)
    # * 匹配正则中前一个字符出现0次或无限次
    # + 匹配正则中前一个字符出现1次或无限次
    # ? 匹配正则中前一个字符出现0次或1次
    # {m} 匹配正则中前一个字符出现m次
    # {m,n} 匹配前正则中一个字符出现m次到n次
    result = re.match(r"速度与激情\d{1,2}", "速度与激情10")
    print("匹配1-2位", result.group())

    result = re.match(r"010-?\d{8}", "010-12345678")
    print("匹配电话，-可有可无", result.group())

    result = re.match(r"https?://\w*\.\w*\.?\w*", "http://www.baidu.com")
    print("匹配任意数量用*", result.group())

    # -------------------------- 匹配开头和结尾 --------------------------
    print("-" * 25, "匹配开头和结尾", "-" * 25)
    # ^ 开头  []中表示不匹配该字符，如[^/]，不匹配/
    # $ 结尾
    result = re.match(".*[.]$", "123.")
    print("是否以.结尾：", result.group())

    # -------------------------- 分组 --------------------------
    print("-" * 25, "分组", "-" * 25)
    # | or
    # () 1、正常括号用作优先级 2、匹配成功后，取出括号中的值
    # (?P<name>...) 分组起名
    # (?P=name) 引用name分组
    ret = re.match(r"[a-zA-Z0-9_]{2,20}@(126|163)\.com$", "llll@163.com")
    print("163或126邮箱：", ret)

    ret = re.match(r"([a-zA-Z0-9_]{2,20})@(126|163)\.com$", "liboxin@163.com")
    print("取出括号中的值：%s 和 %s" % (ret.group(1), ret.group(2)))

    ret = re.match(r"<(\w+).*</\1>", "<h1>hahaha</h1>")
    print("利用分组获取前后是否一致：", ret.group())  # \1代表匹配前面前一个括号分组里一样的值

    ret = re.match(r"<(?P<part1>\w+).*</(?P=part1)>", "<h1>hahaha</h1>")
    print("分组别名：", ret.group())

    # -------------------------- py中re的高级用法 --------------------------
    print("-" * 25, "py中re的高级用法", "-" * 25)

    ret = re.search(r"\d+", "阅读数为：9999")
    print("search不会从头查找 ：", ret.group())

    ret = re.findall(r"\d+", "阅读数为：9999,点赞数为：8888")
    print("findall查找多个 ：%s" % ret)

    ret = re.sub(r"\d+", "10w", "阅读数为：999,点赞数为：8888")
    print("替换 ：%s" % ret)

    ret = re.sub(r"\d+", add, "阅读数为：999,点赞数为：8888")
    print("高级替换 ：%s" % ret)

    ret = re.split(r":| ", "info:xiaoZhang 33 shandong")
    print("以：或 切割", ret)

    # -------------------------- 贪婪与非贪婪 --------------------------
    print("-" * 25, "贪婪与非贪婪", "-" * 25)
    # Python里数量词默认是贪婪的（在少数语言里也可能是默认非贪婪），总是尝试匹配尽可能多的字符；
    # 非贪婪则相反，总是尝试匹配尽可能少的字符。
    # 在"*","?","+","{m,n}"后面加上？，使贪婪变成非贪婪。
    ret = re.match(r"\d{2,4}", "123456")
    ret1 = re.match(r"\d{2,4}?", "123456")
    print(ret.group(), "  ", ret1.group())


def add(temp):
    print("temp=", temp)
    return "100w"


if __name__ == '__main__':
    main()
    # r  原生字符串
    print("c:\\a")
    print(r"c:\\a")
