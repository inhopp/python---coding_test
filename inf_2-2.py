import sys
#sys.stdin = open('input.txt', 'rt') # read text

T = int(input())

for i in range(T):
    n, s, e, k = map(int, input().split())
    number = list(map(int, input().split()))
    sub_list = number[s-1:e]
    sub_list.sort()
    print("#%d %d" %(i+1, sub_list[k-1]))
