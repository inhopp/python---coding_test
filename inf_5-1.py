import sys
#sys.stdin = open('input.txt', 'rt') # read text

n, m = map(int, input().split())
numbers = list(map(int, str(n)))
result = []

for x in numbers:
    while result and m>0 and result[-1]<x:
        result.pop()
        m -= 1
    result.append(x)

if m == 0:
    for x in result:
        print(x, end='')
else:
    for x in result[:-m]:
        print(x, end='')
print()