def test():
    raise MemoryError("啦啦啦")  # 主动抛出一个异常


try:
    test()
except ZeroDivisionError:
    print("异常啦1")
except (IndentationError, IndexError):
    print("异常啦2")
except Exception as e:
    print("未知异常 -> %s" % e)
else:
    print("没有任何异常")
finally:
    print("finally")


import  py_12_模块 as a