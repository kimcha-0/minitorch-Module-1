"""
Collection of the core mathematical operators used throughout the code base.
"""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.
def mul(a: float, b: float) -> float:
    return a * b


def id(a: any) -> any:
    return a


def add(a: float, b: float) -> float:
    return a + b


def neg(a: float) -> float:
    return -a


def lt(a: float, b: float) -> float:
    return a < b


def eq(a: float, b: float) -> float:
    return a == b


def max(a: float, b: float) -> float:
    return a if a > b else b


def is_close(a: float, b: float) -> float:
    return abs(a - b) < .01


def sigmoid(a: float) -> float:
    if a >= 0:
        return 1 / (1 + math.exp(-a))
    else:
        return math.exp(a) / (1 + math.exp(a))


def relu(a: float) -> float:
    return a if a >= 0 else 0


def log(a: float) -> float:
    return math.log(a)


def exp(a: float) -> float:
    return math.exp(a)


def inv(a: float) -> float:
    return 1 / a


def log_back(a: float, b: float) -> float:
    return b / a


def inv_back(a: float, b: float) -> float:
    return -b / a ** 2


def relu_back(a: float, b: float) -> float:
    return b if a >= 0 else 0


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#

def map(
        arr: Iterable[float], fn: Callable[[float], bool]
        ) -> Iterable[float]:
    ret = []
    for i in range(len(arr)):
        ret.append(fn(arr[i]))
    return ret


def zipWith(
        arr1: Iterable[float], arr2: Iterable[float], fn: Callable[[float, float], float]
        ) -> Iterable[float]:
    ret = []
    if len(arr1) != len(arr2):
        raise ValueError(arr1, arr2)
    for i in range(len(arr1)):
        ret.append(fn(arr1[i], arr2[i]))
    return ret


def reduce(
        arr: Iterable[float], fn: Callable[[float, float], float]
        ) -> float:
    result = [i for i in arr]
    for i in range(len(arr)-1):
        result[i+1] = fn(result[i], result[i+1])
    return result[len(arr) - 1] if len(arr) > 0 else 0.0

# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


# TODO: Implement for Task 0.3.
def negList(arr: Iterable[float]):
    return map(arr, neg)


def addLists(arr1: Iterable[float], arr2: Iterable[float]):
    return zipWith(arr1, arr2, add)


def sum(arr: Iterable[float]):
    return reduce(arr, add)


def prod(arr: Iterable[float]) -> float:
    return reduce(arr, mul)
