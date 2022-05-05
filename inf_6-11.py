import sys
#sys.stdin = open('input.txt', 'rt') # read text


def DFS(index, sum, count):
    global result
    if index>n or count>k:
        return

    if count == k:
        if sum%m == 0:
            result += 1

    else:
        DFS(index+1, sum+numbers[index], count+1)
        DFS(index+1, sum, count)


n ,k = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.append(0)
m = int(input())
result = 0
DFS(0,0,0)
print(result)