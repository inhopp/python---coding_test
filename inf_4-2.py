import sys
#sys.stdin = open('input.txt', 'rt') # read text

k, n = map(int, input().split())
numbers = []
for i in range(k):
    numbers.append(int(input()))

max_length = max(numbers)

lt = 0
rt = max_length

while(lt <= rt):
    sum = 0
    mid = (lt + rt) // 2
    
    for i in range(k):
        sum += numbers[i]//mid

    if sum < n :
        rt = mid - 1

    else:
        lt = mid + 1

print(mid)