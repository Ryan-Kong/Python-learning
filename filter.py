'''def is_odd(n):
    return n % 2 == 1
a = list(filter(is_odd,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))  # 高级函数filter将满足条件的元素进行过滤
print(a)

def not_empty(s):
    return s and s.strip()
b = list (filter(not_empty,['a','b','   ',None,'c','None']))
print(b)
'''
# 计算素数
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
def _not_divisible(n):
    return lambda x : x % n > 0
def primes():
    yield 2
    it = _odd_iter()    # 初始数列
    while True:
        n = next(it)    # 返回数列的第一个数
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列
for n in primes(): # 打印1000以内的素数；
    if n < 1000:
        print (n)
    else:
        break