# -*- coding: utf-8 -*-
"""
Created on Sun May 27 16:12:04 2018

@author: vincent
"""
from functools import wraps

def memo(func):
    cache = {}
    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap

@memo
def fib(i):
    if i<2: return 1
    return fib(i-1)+fib(i-2)

print(fib(100))
