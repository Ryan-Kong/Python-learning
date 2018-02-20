def power(x,n = 2): # n为默认参数，在初始时赋值2
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power(5))