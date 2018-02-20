# _*_ coding: utf_8 _*_
L = [3,4,67,12,123,65,4567,0,999,1000 ]
def findMinandMax(L):
    max = L[0]
    min = L[0]
    for x in L:
        if x > max:
            return max
    for y in L:
        if y < min:
            return min

    #print (x,y)
print (findMinandMax(max,min))