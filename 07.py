import functools
import math


def gcd(a: 'int', b: 'int') -> 'int':
    while b:
        a %= b
        a, b = b, a
    return a


def egcd(a: 'int', b: 'int') -> 'tuple':
    if a == 0:
        return b, 0, 1
    d, x1, y1 = egcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return d, x, y


def str_base(value: 'int', base: 'int') -> 'str':
    """Shows value using number base, e.g. str_base(44027, 36)=='XYZ'"""
    if base <= 10:
        return str(value)
    if base <= 36:
        res = ""
        while value > 0:
            digit = value % base
            if digit < 10:
                res += str(digit)
            else:
                res += chr(value % base + ord('A') - 10)
            value //= base
        return res[::-1]
    else:
        return "Error"


def is_simple(value: 'int') -> 'bool':
    if value == 2:
        return True
    if value % 2 == 0 or value == 1:
        return False
    for i in range(3, round(math.sqrt(value)), 2):
        if value % i == 0:
            return False
    return True


is_simple_cached = functools.lru_cache()(is_simple)
