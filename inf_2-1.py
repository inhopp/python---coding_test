import sys
#sys.stdin = open('input.txt', 'rt') # read text

n, k = map(int,input().split())

cand = []
for i in range(1, n+1):
    if n%i == 0:
        cand.append(i)

if k > len(cand):
    print(-1)
else:
    print(cand[k-1])
