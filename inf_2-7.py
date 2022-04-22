import sys
#sys.stdin = open('input.txt', 'rt') # read text

n = int(input())

check_prime = [0] * (n+1)
count = 0

for i in range(2, n+1):
    if check_prime[i] == 0:
        count += 1
        for j in range(i, n+1, i):
            check_prime[j] = 1

print(count)