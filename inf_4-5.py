import sys
#sys.stdin = open('input.txt', 'rt') # read text

n = int(input())
numbers = []
for i in range(n):
    numbers.append(list(map(int, input().split())))

numbers.sort(key=lambda x:x[0], reverse=True)

count = 1
for i in range(1, n):
    check_flag = True
    for j in range(i):
        if numbers[i][1] < numbers[j][1]:
            check_flag = False
            break
    if check_flag:
        count += 1

print(count)