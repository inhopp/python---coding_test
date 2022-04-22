import sys
#sys.stdin = open('input.txt', 'rt') # read text

n = int(input())
apple = [[0]*n for _ in range(n)]
for i in range(n):
    apple[i] = list(map(int, input().split()))

sum = 0
m = n//2

for i in range(n):
    if i <= m:
        for j in range(i+1):
            if j == 0:
                sum += apple[i][m]
            else:
                sum += apple[i][m-j]
                sum += apple[i][m+j]

    else:
        for j in range((2*m) - i + 1):
            if j == 0:
                sum += apple[i][m]
            else:
                sum += apple[i][m-j]
                sum += apple[i][m+j]

                
print(sum)