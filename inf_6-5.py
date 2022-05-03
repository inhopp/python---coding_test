import sys
#sys.stdin = open('input.txt', 'rt') # read text

def DFS(index, sum):
    global result

    if sum > c:
        return

    if index == n:
        if sum > result:
            result = sum

    else:
        DFS(index+1, sum + numbers[index])
        DFS(index+1, sum)

           
c, n = map(int, input().split())
numbers = []
for _ in range(n):
    numbers.append(int(input()))

total = sum(numbers)
result = 0

DFS(0, 0)
print(result)