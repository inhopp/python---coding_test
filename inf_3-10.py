import sys
#sys.stdin = open('input.txt', 'rt') # read text

numbers = [list(map(int, input().split())) for _ in range(9)]

def check(a):
    for i in range(9):
        row_check = [0] * 9
        col_check = [0] * 9

        for j in range(9):
            row_check[a[i][j] - 1] = 1
            col_check[a[j][i] - 1] = 1

        if sum(row_check) != 9 or sum(col_check) != 9:
            return False

    for i in range(3):
        for j in range(3):
            box_check = [0] * 9

            for k in range(3):
                for l in range(3):
                    box_check[a[(3*i)+k][(3*j)+l] - 1] = 1

            if sum(box_check) != 9:
                return False

    return True

result = check(numbers)
if result: print('YES')
else: print('NO')