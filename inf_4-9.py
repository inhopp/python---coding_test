import sys
#sys.stdin = open('input.txt', 'rt') # read text

n = int(input())
numbers = list(map(int, input().split()))

result_pos = []
last_value = 0
count = 0

while numbers:
    L = len(numbers)

    if last_value > max(numbers[0], numbers[L-1]):
        break

    elif last_value < min(numbers[0], numbers[L-1]):
        if numbers[0] < numbers[L-1]:
            last_value = numbers[0]
            result_pos.append('L')
            numbers.pop(0)
            count += 1
        else:
            last_value = numbers[L-1]
            result_pos.append('R')
            numbers.pop()
            count += 1

    else:
        if last_value < numbers[0]:
            last_value = numbers[0]
            result_pos.append('L')
            numbers.pop(0)
            count += 1

        elif last_value < numbers[L-1]:
            last_value = numbers[L-1]
            result_pos.append('R')
            numbers.pop()
            count += 1

print(count)
for i in range(count):
    print(result_pos[i], end='')
print()