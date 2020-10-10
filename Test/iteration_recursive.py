# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 21:13:54 2020

@author: HP
"""




def f(x):
    x = 4
    def g(y):
        def h(z):
            nonlocal x
            x = x + 1
            return x + y + z
        return h
    return g
a = f(1)
b = a(2)
total=b(3)+b(4) #total=22, b point to h function, twice call h

# 231
# 23
# 2
# 23
# 231
def cascade(n): # not clarify
    print(n)
    if n>=10:
        cascade(floor(n/10))
        print(n)
#the second methods
def cascade(n):
    if n<10:
        print(n)
    else:
        print(n)
        cascade(n//10)
        print(n)
# iteration
def fact(n):
    total,k=1,1
    while k<=n:
        total, k=total*k, k+1
    return total
# iteration to recursive is formulaic
# recursive to iteratoin is more tricky
#recursion
def fact1(n):
    if n == 0 :
        return 1
    else:
        return fact1(n-1)*n

