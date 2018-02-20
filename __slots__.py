class Student(object):
  __slots__ = ('name', 'age')   # 定义一个特殊的__slots__变量，来限制该class实例能添加的属性

# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的