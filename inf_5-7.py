import sys
#sys.stdin = open('input.txt', 'rt') # read text

ness = list(input())
n = int(input())
cand = []
result = []

for i in range(n):
    cand.append(list(input()))
    
for i in range(n):
    ness_cand = ness[:]
    flag = True

    for x in cand[i]:
        if x in ness_cand:
            if x != ness_cand.pop(0):
                flag = False
                break

    if flag and (not ness_cand):
        result.append('YES')
    else:
        result.append('NO')


for i in range(n):
    print("#%d %s" %(i+1, result[i]))