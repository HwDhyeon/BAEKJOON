# https://www.acmicpc.net/problem/2908

a, b = input().split()
print(sorted([int(a[::-1]), int(b[::-1])])[-1])
