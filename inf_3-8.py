import sys
#sys.stdin = open('input.txt', 'rt') # read text

n = int(input())
numbers = [list(map(int, input().split())) for _ in range(n)]

m = int(input())
shifted = [0] * n

for i in range(m):
    cmd = list(map(int, input().split()))

    if cmd[1] == 0:
        for j in range(n):
            stride = (j + cmd[2]) % n
            shifted[j] = numbers[cmd[0]-1][stride]
    
    else:
        for j in range(n):
            stride = (j + (n - cmd[2])) % n
            shifted[j] = numbers[cmd[0]-1][stride]

    for j in range(n):
        numbers[cmd[0]-1][j] = shifted[j]


sum = 0
s = 0
e = n
for i in range(n):
    for j in range(s, e):
        sum += numbers[i][j]

    if i < n//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(sum)