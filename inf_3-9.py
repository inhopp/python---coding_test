import sys
#sys.stdin = open('input.txt', 'rt') # read text

n = int(input())
numbers = [[0] * n for _ in range(n)]
for i in range(n):
    numbers[i] = list(map(int, input().split()))

padding_numbers = [[0] * (n+2) for _ in range(n+2)]
for i in range(1,n+1):
    for j in range(1, n+1):
        padding_numbers[i][j] = numbers[i-1][j-1]

count = 0
for i in range(1,n+1):
    for j in range(1, n+1):
        check_flag = True
        m = padding_numbers[i][j]
        if m <= padding_numbers[i-1][j]: 
            check_flag=False
        elif m <= padding_numbers[i][j-1]: 
            check_flag=False
        elif m <= padding_numbers[i][j+1]: 
            check_flag=False
        elif m <= padding_numbers[i+1][j]: 
            check_flag=False

        if check_flag:
            count += 1

print(count)