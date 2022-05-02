import sys
#sys.stdin = open('input.txt', 'rt') # read text

def DFS(index, sum):
    if sum > total//2:
        return

    if index == n:
        if sum == total-sum:
            print("YES")
            sys.exit(0)

    else:
        DFS(index+1, sum + numbers[index])
        DFS(index+1, sum)

           

n = int(input())
numbers = list(map(int, input().split()))
total = sum(numbers)

DFS(0, 0)
print("NO")