import sys
#sys.stdin = open('input.txt', 'rt') # read text

n, k = map(int, input().split())
number = list(map(int, input().split()))

result = set()
sum = 0

for i in range(n):
    for j in range(i+1, n):
        for l in range(j+1,n):
            sum = number[i] + number[j] + number[l]
            result.add(sum)
            
result = list(result)
result.sort(reverse = True)
print(result[k-1])