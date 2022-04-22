import sys
#sys.stdin = open('input.txt', 'rt') # read text

result = []
for i in range(2):
    n = int(input())
    numbers = list(map(int, input().split()))
    result += numbers

result.sort()
for i in range(len(result)):
    print(result[i], end=' ')