L = ['a','b','c','d','e','f']   # 列表可变
print(L[0:3])   # 取列表L的前3个元素
print(L[:3])    # 还是取前三个元素
print(L[-6:-3]) # 还是前三个元素
T = ('a','b','c','d','e','f')   # 元祖不可变
print(T[0:3])   # 元祖也可以切片操作
a = 'abcdefghijklmnopqrstuvwxyz'    # 字符串也可以操作切片
print(a[:3])