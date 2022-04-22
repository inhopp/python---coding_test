import sys
#sys.stdin = open('input.txt', 'rt') # read text

n = int(input())
numbers = list(map(int, input().split()))

def reverse(x):
    str_num = str(x)
    reverse_str = str_num[::-1]
    return int(reverse_str)

def isPrime(x):
    if x == 1: return False

    root_x = round(x**(1/2))

    for i in range(2, root_x+1):
        if x % i == 0:
            return False

    return True

for i in range(n):
    reverse_n = reverse(numbers[i])
    if isPrime(reverse_n):
        print(reverse_n, end=" ")