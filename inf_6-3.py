import sys
#sys.stdin = open('input.txt', 'rt') # read text

def ST(v):
    if v > n:
        for i in range(1, n+1):
            if check_box[i] == 1:
                print(i, end=' ')
        print()

    else:
        check_box[v] = 1
        ST(v+1)

        check_box[v] = 0
        ST(v+1)

n = int(input())
check_box = [0]*(n+1)
ST(1)