# https://www.acmicpc.net/problem/10818

input()
r = list(map(int, input().split()))
print(min(r), max(r))

# 다른 답

print(min(s:=[*map(int,[*open(0)][1].split())]),max(s))