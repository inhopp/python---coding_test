import sys
#sys.stdin = open('input.txt', 'rt') # read text

n, m = map(int, input().split())

proba = [0] * (n+m)
result = []

for i in range(n):
    for j in range(m):
        sum = (i+1) + (j+1)
        proba[sum-1] += round((1/n)+(1/m),2)

for i in range(len(proba)):
    if proba[i] == max(proba):
        result.append(i+1)

for i in range(len(result)):
    print(result[i], end=" ")