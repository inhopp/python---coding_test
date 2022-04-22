import sys
#sys.stdin = open('input.txt', 'rt') # read text

n = int(input())
scores = list(map(int, input().split()))

avg = sum(scores)/n
avg = round(avg)

min = 10000
origin_socre = 0

for i in range(n):
    m = abs(scores[i] - avg)
    if min > m:
        min = m
        origin_socre = scores[i]
        index = i+1
    
    elif min == m:
        if origin_socre < scores[i]:
            origin_socre = scores[i]
            index = i+1

print(avg, index)