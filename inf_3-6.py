import sys
from typing import List
#sys.stdin = open('input.txt', 'rt') # read text

n = int(input())
matrix = [[0]*n for _ in range(n)]

for i in range(n):
    matrix[i] = list(map(int, input().split()))

cand_sum = [0] * (2*n + 2)

for i in range(n):
    for j in range(n):
        cand_sum[i] += matrix[i][j]     # sum of rows
        cand_sum[n+j] += matrix[i][j]   # sum of columns
        if i == j:
            cand_sum[2*n] += matrix[i][j]
        if i + j == 4:
            cand_sum[2*n + 1] += matrix[i][j]


print(max(cand_sum))