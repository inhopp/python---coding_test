import sys
#sys.stdin = open('input.txt', 'rt') # read text

n, m = map(int, input().split())
l = list(map(int, input().split()))

count = 0
cur = m

while True:
    if l[0] == max(l):
        count += 1

        if cur == 0:
            break
        else:
            l.pop(0)
            cur -= 1
    
    else:
        l.append(l.pop(0))
        if cur == 0:
            cur = len(l)-1
        else:
            cur -= 1

print(count)