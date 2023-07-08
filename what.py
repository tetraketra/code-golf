from typing import get_type_hints
from dataclasses import dataclass
import typing
import __main__
import inspect
import weakref
import random



# ==========

# x = 10
# while (x := (x := (x := x - 1) - 1) - 1) > 0: print(x)

# ==========

# def λ(code):
#     return eval(f"lambda {code}")

# print(λ("x, y: x + 1 + y")(10, 20))

# ==========

# from what2 import big_func, hi
# print(inspect.getsourcefile(big_func))
# print(inspect.getsource(big_func))
# print(inspect.getsourcelines(big_func))

# ==========

# # hi there
# def example_func(input: list[int, ...]) -> int:
#     """doc string"""
#     ...
# print(inspect.getdoc(example_func))
# print(inspect.getcomments(example_func))
# print(dict(inspect.getmembers(example_func))["__annotations__"])

# ==========

# @dataclass
# class test():
#     a: int
# @dataclass
# class test2(test):
#     b: int
# [print(x) for x in inspect.getclasstree([test2])]

# ==========

# a = 10
# def outer():
#     b = 7
#     def inner():
#         c = 5
#         print(a, b, c)
#     inner()
#     print(inspect.getclosurevars(inner))
# outer()

# print = 8
# print(8)

# ==========

# var: 5 = 10
# print(var)
# print(get_type_hints(__main__))
# print(dict(inspect.getmembers(var)).keys())

# var: (x := 7) = 10
# print(var, x)
# print(get_type_hints(__main__))

# ==========

# from itertools import count
# a: [i for i in count(0)] = 10

# ==========

# print((lambda x: x + 1)(20))
# var: print((lambda f: [f.read(), f.close()][0])(open(__file__, "r"))) = None
# print(get_type_hints(__main__))

# ==========

@dataclass
class ex():
    num: int

# a = ex(10)
# b = a
# del a
# print(b)

# a = ex(10)
# b = weakref.ref(a)
# print(b)
# del a
# print(b)

# a = ex(10)
# def when_garbaged():
#     print("gone!")
# whatever = weakref.finalize(a, when_garbaged)
# setattr(whatever, "atexit", False)
# a.num += 10
# a = 100

# ==========

# def example1() -> int:
#     ...
# def example2() -> dict(inspect.getmembers(example1))["__annotations__"]['return']:
#     ...

# dict(inspect.getmembers(example2))["__annotations__"]['return'] = str

# b: dict(inspect.getmembers(example2))["__annotations__"]['return'] = 12
# # print(type(b))

# a: get_type_hints(__main__)['b'] = 10
# print(get_type_hints(__main__))

# ==========

# a = a[0] = [1]
# print(a)
# print(a, a[0])

# a.append(2)
# print(a, a[0])

# print(a[0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][0][1])

# # ==========


e = 10

try:
    1/0
except ZeroDivisionError as b:
    print()

print(b)