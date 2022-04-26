import sys
#sys.stdin = open('input.txt', 'rt') # read text

n = int(input())
numbers = list(map(int, input().split()))
m = int(input())

for i in range(m):
    max_val = max(numbers)
    min_val = min(numbers)

    for j in range(n):
        if numbers[j] == max_val:
            max_index = j
        if numbers[j] == min_val:
            min_index = j

    numbers[max_index] -= 1
    numbers[min_index] += 1

print(max(numbers) - min(numbers))