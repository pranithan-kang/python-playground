#! pip install plum_dispatch

from typing import Callable
from plum import dispatch


@dispatch
def my_func(a: int):
    print("this is one param func")


@dispatch
def my_func(a: int, b: int):
    print("this is two param func")


@dispatch
def my_func(func: Callable, a: int):
    print(f"this is function with lambda 1 arg {func(a)}")


my_func(1)

my_func(2)

my_func(3, 4)

my_func(lambda x: x + 10, 1234)
