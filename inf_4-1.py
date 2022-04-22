import sys
#sys.stdin = open('input.txt', 'rt') # read text

n, m =map(int, input().split())
numbers = list(map(int, input().split()))

def binary_search(lt, rt, m, numbers):
    mid = (lt + rt) // 2

    if numbers[mid] == m:
        return mid

    elif numbers[mid] > m:
        return binary_search(lt, mid-1, m, numbers)

    else:
        return binary_search(mid+1, rt, m, numbers)


numbers.sort()
result = binary_search(0, n-1, m, numbers)
print(result + 1)
