import sys
#sys.stdin = open('input.txt', 'rt') # read text

def DFS(depth):
    global count

    if depth > n:
        return

    if depth == m:
        for i in range(depth):
            print(result[i], end=" ")
        print()
        count += 1

    else:
        for i in range(1, n+1):
            if check_list[i] == 0:
                check_list[i] = 1
                result[depth] = i
                DFS(depth+1)
                check_list[i] = 0


n, m = map(int, input().split())
check_list = [0] * (n+1)
result = [0] * n
count = 0

DFS(0)
print(count)