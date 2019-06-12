# -------------------------- 拓展一个字段？！用法 --------------------------
print("-" * 25, "拓展一个字段？！", "-" * 25)


class Cat:

    def __init__(self):
        print("我在初始化时执行")

    def eat(self):
        print("%s爱吃鱼" % self.name)  # 这里可以使用外面拓展的字段,因为是编译型语言

    def drink(self):
        print("%s要喝水" % self.name)

    def __del__(self):
        print("我在销毁时执行")

    def __str__(self):  # toString（）
        return "__str__ -> %s" % self.name


tom = Cat()
tom.name = "小咪咪"  # 这里可以定义一个字段，class里并没有的字段
tom.eat()
tom.drink()
print(tom)
del tom
# -------------------------- 上面的做法是错误的 --------------------------
print("-" * 25, "上面的做法是错误的", "-" * 25)


class Dog:

    def __init__(self, name):
        # self.name = ""
        self.name = name

    def eat(self):
        print("%s爱吃骨头" % self.name)

    def drink(self):
        print("%s要喝水" % self.name)


tom = Dog("小汪汪")
# tom.name = "小汪汪"
tom.eat()
tom.drink()

# -------------------------- 继承 --------------------------
print("-" * 25, "继承", "-" * 25)


class Animal:
    def eat(self):
        print("动物可以吃东西")


class XiaoTianDog(Dog, Animal):
    def __init__(self):
        super(XiaoTianDog, self).__init__("哮天犬")
        print("我是一条哮天犬,我出生了")

    def eat(self):  # 方法重写
        super(XiaoTianDog, self).eat()
        # Dog.eat(self)  # 这是python2.X的调用父类的方法
        print("我也爱吃妖怪")

    def empty_method(self):
        pass  # pass是占位


xiaoTianDog = XiaoTianDog()
xiaoTianDog.eat()
xiaoTianDog.drink()
xiaoTianDog.empty_method()

# -------------------------- 私有属性和私有方法 --------------------------
print("-" * 25, "私有属性和私有方法", "-" * 25)


class People:
    def __init__(self):
        self.name = "张三"
        self.__money = "100W"  # __代表私有属性

    def __private_method(self):
        print("我是私有的方法，你调用不到")


people = People()
print(people.name)
# print(people.__money)  # 这里会报错
# -------------------------- 类成员属性 --------------------------
print("-" * 25, "类成员属性", "-" * 25)


class Tools:
    count = 0  # 相当于静态的，记录的是类的特征而不是对象特征

    def __init__(self):
        Tools.count += 1  # 类名.属性名

    @classmethod
    def class_method(cls):  # 这里用cls做参数
        print("我是类方法，直接 类名.方法名 调用,可以访问类属性")

    @staticmethod
    def static_method():
        print("我是静态方法，参数里是空的,什么都不需要访问时可以用我")


斧子 = Tools()
锯子 = Tools()
print(Tools.count)
# print(斧子.count)  # 也可以使用变量名访问,不推荐
Tools.class_method()
Tools.static_method()
