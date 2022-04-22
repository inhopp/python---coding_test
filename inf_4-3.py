import sys
#sys.stdin = open('input.txt', 'rt') # read text

n, m = map(int, input().split())
numbers = list(map(int, input().split()))

result = sum(numbers) // m

def check(result):
    sum = 0
    count = 1

    for i in range(n):
        sum += numbers[i]

        if sum > result:
            count += 1
            sum = numbers[i]

    return count


while(check(result) != m):
    result += 1

print(result)