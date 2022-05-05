import sys
#sys.stdin = open('input.txt', 'rt') # read text

def DFS(index, score, time):
    global result

    if time>m:
        return

    if index == n:
        if score > result:
            result = score

    else:
        DFS(index+1, score+problem[index][0], time+problem[index][1])
        DFS(index+1, score, time)


n, m = map(int, input().split())
problem = []
for _ in range(n):
    l = list(map(int, input().split()))
    problem.append(l)

result = 0
DFS(0,0,0)
print(result)