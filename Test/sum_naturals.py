# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 14:03:13 2020

@author: HP
"""

def make_greeter(name):
    return lambda greet:print(greet, name)
make_greeter("Tony")
greet_funciton = make_greeter("Tony")
make_greeter("Tony")("Hi")

# 我调我自己
# def print_num(n):
#     print(n)
#     def next_num(k):
#         return print_num(n+k)
#     return next_num
# print_num(1)(2)(5)


# def make_adder(n):
#     def adder(k):
#         return k+n
#     return adder
# def square(x):
#     return x*x
# def composel(f, g):
#     def h(x):
#         return f(g(x))
#     return h
# print(composel(square, make_adder(2))(3)) #print its result in screen

