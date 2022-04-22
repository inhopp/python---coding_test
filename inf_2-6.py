import sys
#sys.stdin = open('input.txt', 'rt') # read text

n = int(input())
numbers = list(map(int, input().split()))

def digit_sum(x):
    sum = 0
    while(True):
        if x//10 == 0:
            sum += x
            break
        else:
            sum += x%10
            x = x//10
    
    return sum

result = []

for i in range(n):
    m = digit_sum(numbers[i])
    result.append(m)


index = result.index(max(result))
print(numbers[index])