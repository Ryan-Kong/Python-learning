class Student(object):  # 定义Student类，（object）表示Student即成object类；

    def __init__(self, name, score):    # 创建实力的时候绑定强制属性， __init__方法的第一个参数永远是self
        self.name = name
        self.score = score

# print(bart.name, ',',bart.score)    # 测试打印bart属性

    def print_score(std):
        print('%s: %s' % (std.name, std.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

lisa = Student('Lisa', 99)
bart = Student('Bart', 59)
print(lisa.name, lisa.get_grade())
print(bart.name, bart.get_grade())

'''
小结

类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响；

方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；

通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。

和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：