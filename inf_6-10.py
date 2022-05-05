import sys
#sys.stdin = open('input.txt', 'rt') # read text

def DFS(depth, position):
    global count

    if depth>m:
        return

    if depth == m:
        for i in range(depth):
            print(numbers[i], end=" ")
        print()
        count += 1

    else:
        for i in range(position, n):
            numbers[depth] = i+1
            DFS(depth+1, i+1)


n, m = map(int, input().split())
numbers = [0] * n
count = 0
DFS(0,0)
print(count)