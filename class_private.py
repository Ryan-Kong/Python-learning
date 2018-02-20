class Student(object):

	def __init__(self,name,score):
		self.__name = name    # 在定义变量时在相应属性前增加两个下划线__，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问，
		self.__score = score   # 将score变为私有变量

	def print_score(self):
		print('%s , %s' % (self.__name, self.__score))

	def get_name(self):    # 定义获取私有变量的方法
		return self.__name

	def get_score(self):
		return self.__score

	def set_score(self,score):     # 允许外部代码更改私有变量的方式
		if 0 <= score <= 100:     # 通过这种方式可以对私有变量增加验证
			self.__score = score
		else:
			raise ValueError('无效的成绩')