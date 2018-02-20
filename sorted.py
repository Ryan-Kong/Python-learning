a = sorted([36, 5, -12, 9, -21])    # sorted函数进行排序
print (a)
b = sorted([36, 5, -12, 9, -21], key=abs)   # sorted可以加入key值进行优化排序
print (b)
c = sorted(['bob', 'about', 'Zoo', 'Credit'])   # 对于字符串也可以进行排序
print (c)
c = sorted(['bob', 'about', 'Zoo', 'Credit'], key = str.lower)  # 加入key值进行优化
print (c)
c = sorted(['bob', 'about', 'Zoo', 'Credit'], key = str.lower, reverse = True)  # 增加反向排序
print (c)
