import sys
#sys.stdin = open('input.txt', 'rt') # read text
import heapq as hq

a = []

while True:
    n = int(input())

    if n == -1:
        break

    elif n == 0:
        if a:
            print(-hq.heappop(a))
        else:
            print(-1)

    else:
        hq.heappush(a, -n)