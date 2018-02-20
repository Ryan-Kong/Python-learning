# _*_ coding: utf_8 _*_
def trim(s):
    while s[:0] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]
    return s
s = 'hell0     '
print(trim(s))