# https://www.acmicpc.net/problem/10809

from string import ascii_lowercase

word = input()
for alphabet in ascii_lowercase:
    print(word.index(alphabet) if alphabet in word else -1, end=' ')
print()
