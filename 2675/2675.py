# https://www.acmicpc.net/problem/2675

n = int(input())

for _ in range(n):
    i, word = input().split()
    for s in word:
        print(s * int(i), end='')
    print()
