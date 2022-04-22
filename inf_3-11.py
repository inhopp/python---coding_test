import sys
#sys.stdin = open('input.txt', 'rt') # read text

numbers = [list(map(int, input().split())) for _ in range(7)]

count = 0

for i in range(7):
    for j in range(3):
        row = numbers[i][j:j+5]

        if row == row[::-1]:
            count += 1
        
        col_flag = True

        for k in range(2):
            if numbers[j+k][i] != numbers[j+5 -k -1][i]:
                col_flag = False
        
        if col_flag:
            count += 1

print(count)