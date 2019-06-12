class Instance:
    instance = None
    init = False  # 防止多次初始化

    def __new__(cls, *args, **kwargs):
        """
        此方法是实例化对象时调用的
        如果这里不调用父类的new方法，则有下列问题：
        1、不走__init__
        2、不能实例化对象，一直都是None
        """
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        if Instance.init:
            return
        print("初始化")


i = Instance()
i1 = Instance()
print(i)
print(i1)
