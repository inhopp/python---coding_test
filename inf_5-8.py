import sys
#sys.stdin = open('input.txt', 'rt') # read text

n = int(input())
cand = []
using = []

for i in range(n):
    cand.append(input())

for i in range(n-1):
    using.append(input())

for x in cand:
    if x not in using:
        result = x
        break

print(result)