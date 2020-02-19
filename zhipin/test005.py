#!/usr/bin/python
# -*- coding: UTF-8 -*-
i = 1;
def foo():
    print("starting...")
    while True:
        i_ = i + 1
        res = yield i_
        print("res:",res)
g = foo()
print(next(g))
print("*"*20)
print(next(g))
