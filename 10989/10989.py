# https://www.acmicpc.net/problem/10989

import sys

n = int(input())
nl = [0] * 10000

for _ in range(n):
    nl[int(sys.stdin.readline()) - 1] += 1

for i in range(10000):
    if nl[i]:
        for j in range(nl[i]):
            print(i+1)
