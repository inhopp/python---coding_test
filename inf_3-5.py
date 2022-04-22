import sys
#sys.stdin = open('input.txt', 'rt') # read text

n, m = map(int, input().split())
numbers = list(map(int, input().split()))

count = 0
lt = 0
rt = 1
sum = numbers[lt]

while(True):
    if sum < m:
        if rt < n:
            sum += numbers[rt]
            rt += 1
        else:
            break

    elif sum == m:
        count += 1
        sum -= numbers[lt]
        lt += 1
    
    else:
        sum -= numbers[lt]
        lt += 1

print(count)