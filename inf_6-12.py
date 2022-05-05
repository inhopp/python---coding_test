import sys
#sys.stdin = open('input.txt', 'rt') # read text

def DFS(v):
    global count

    if v == n:
        count += 1
        return

    else:
        for i in range(1,n+1):
            if check[i]==0 and graph[v][i]==1:
                check[i] = 1
                path.append(i)
                DFS(i)
                check[i] = 0
                path.pop()


n, m = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    i, j = map(int, input().split())
    graph[i][j] = 1

check = [0]*(n+1)
check[1] = 1
path = [1]
count = 0
DFS(1)
print(count)