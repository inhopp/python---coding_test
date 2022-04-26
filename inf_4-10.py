import sys
#sys.stdin = open('input.txt', 'rt') # read text

n = int(input())
numbers = list(map(int, input().split()))
result = [0]*n

for i in range(n):
    count = 0

    for j in range(n):
        if result[j] != 0:
            continue

        else:
            if numbers[i] == count:
                result[j] = i+1
                break

            else:
                count += 1

for i in range(n):
    print(result[i], end=' ')
print()