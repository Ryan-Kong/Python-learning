# _*_ coding: utf_8 _*_
# 匿名函数: lambda x:
'''
    改造原始函数：


    def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))
'''
'''
L = list(filter(lambda x : x % 2 == 1, range(1,20)))
print (L)

'''
# 面向对象编程的实例
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def print_score(self):
        print('%s: %s' % (self.name, self.score))
bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()
'''
'''
'''
# 私有变量练习
# 请把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性：
class Student(object):
    def __inti__(self, name, gender):
        self.name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        if gender == 'Female' or gender == 'Male':
            self.__gender = gender
        else:
            raise GenderError('性别错误')