# _*_ coding: utf_8 _*_
# 匿名函数: lambda x:
'''
    改造原始函数：
    def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))

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