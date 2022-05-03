import sys
#sys.stdin = open('input.txt', 'rt') # read text

def DFS(count, sum):
    global result

    if sum > total or count > result:
        return

    if sum == total:
        if result > count:
            result = count

    else:
        for i in range(n):
            DFS(count+1, sum + coins[i])


n = int(input())
coins = list(map(int, input().split()))
total = int(input())
result = 10000
coins.sort(reverse=True)

DFS(0,0)
print(result)