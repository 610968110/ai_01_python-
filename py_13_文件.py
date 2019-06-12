# -------------------------- 读文件 --------------------------
print("-" * 25, "读文件", "-" * 25)
file = open("filetest.txt")  # 默认只读方式的打开
print(file.read())  # read会移动文件的指针，再次read就不行了
file.close()

# -------------------------- 读文件2 --------------------------
print("-" * 25, "读文件2", "-" * 25)
file = open("filetest.txt")
print(file.read(5))  # 读取的长度
file.close()
# -------------------------- 写文件 --------------------------
print("-" * 25, "写文件", "-" * 25)
file = open("filetest.txt", "w")  # 可写
file.write("1234567890")  # 会覆盖文件内容，如果文件不存在则新建文件
file.close()
# -------------------------- 写文件2 --------------------------
print("-" * 25, "写文件2", "-" * 25)
file = open("filetest.txt", "a")  # 追加在文件内容后面写
file.write("\n嘤嘤嘤")
file.close()
# -------------------------- readLine --------------------------
print("-" * 25, "readLine", "-" * 25)
file = open("filetest.txt")
print("第一行 -> %s" % file.readline())  # readLines则是返回列表
print("第二行 -> %s" % file.readline())
file.close()
# -------------------------- 重命名、创建目录、判断是否是文件等 --------------------------
print("-" * 25, "重命名、创建目录、判断是否是文件等", "-" * 25)
import  os
# os.mkdir("...")
# os.rename("...")
