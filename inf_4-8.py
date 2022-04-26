import sys
#sys.stdin = open('input.txt', 'rt') # read text

n, m = map(int, input().split())
weights = list(map(int, input().split()))

weights.sort()
count = 0

while len(weights)>0:
    L = len(weights)
    count += 1

    if L == 1:
        break

    elif weights[0] + weights[L-1] > m:
        weights.pop()
    
    else:
        weights.pop()
        weights.pop(0)

print(count)