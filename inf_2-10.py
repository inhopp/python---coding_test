import sys
#sys.stdin = open('input.txt', 'rt') # read text

n = int(input())
result = list(map(int, input().split()))

count = 0
score = 0
for i in range(n):
    if result[i] == 1:
        count += 1
        score += count
    else:
        count = 0

print(score)