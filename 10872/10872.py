# https://www.acmicpc.net/problem/10872

from functools import cache

@cache
def fac(n):
    return n * fac(n-1) if n else 1

print(fac(int(input())))
