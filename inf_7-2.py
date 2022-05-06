import sys
#sys.stdin = open('input.txt', 'rt') # read text

def DFS(date, sum):
    global result
    
    if date > n:
        return

    if result < sum:
        result = sum


    for i in range(date, n):
        DFS(date+(i-date)+l[i][0], sum+l[i][1])



n = int(input())
l = []
for i in range(n):
    t, p = map(int, input().split())
    l.append([t, p])
result = 0
DFS(0,0)
print(result)