import sys
#sys.stdin = open('input.txt', 'rt') # read text

n, k = map(int, input().split())
l = []

for i in range(n):
    l.append(i+1)

check = 1

while len(l) > 1:
    if k != check:
        l.append(l.pop(0))
        check += 1

    else:
        l.pop(0)
        check = 1

print(l[0])