import sys
#sys.stdin = open('input.txt', 'rt') # read text

n = int(input())

for i in range(n):
    str1 = input()
    str2 = str1[::-1]

    if str1.upper() == str2.upper():
        print("#%d YES" %(i+1))
    else:
        print("#%d NO" %(i+1))