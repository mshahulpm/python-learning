from util import print_name
from mypy import argmap


def greet(name: str) -> None:
    print("Hello ", name)
    print_name("")
    print(type(argmap))


def sum(n1: int | None, n2: int) -> int:
    if not n1:
        return 0
    return n1 + n2


def hello() -> None:
    print("hello")


greet("")
