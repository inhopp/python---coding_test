import sys
#sys.stdin = open('input.txt', 'rt') # read text

def DFS(L):
    if L > n:
        return

    if L == n:
        sum = 0
        for i in range(n):
            sum += numbers[i]*c[i]
        
        if sum == f:
            for x in numbers:
                print(x, end=" ")
            print()
            sys.exit(0)

    else:
        for i in range(1, n+1):
            if check[i] == 0:
                numbers[L] = i
                check[i] = 1
                DFS(L+1)
                check[i] = 0


n, f = map(int, input().split())
check = [0] * (n+1)
numbers = [0] * n
c = [1] * n
for i in range(1, n):
    c[i] = c[i-1]*(n-i)//i
result = []

DFS(0)
