# BAEKJOON: 2588번 문제 (곱셈)
# https://www.acmicpc.net/problem/2588

a = int(input())
b = int(input())
print("%d\n%d\n%d\n%d"%((a * (b % 10)), (a * ((b % 100)//10)), (a * (b//100)), (a * b)))
