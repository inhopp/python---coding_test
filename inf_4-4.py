import sys
#sys.stdin = open('input.txt', 'rt') # read text

n, c = map(int, input().split())
pos = []
for i in range(n):
    pos.append(int(input()))
pos.sort()

def count(mid):
    cnt = 1
    end_point = pos[0]

    for i in range(1, n):
        if pos[i] - end_point >= mid:
            end_point = pos[i]
            cnt += 1

    return cnt

lt = pos[0]
rt = pos[n-1]

while lt <= rt:
    mid = (lt + rt) // 2
    if count(mid) < c:
        rt = mid - 1
    else:
        result = mid
        lt = mid + 1
        

print(result)