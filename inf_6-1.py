import sys
#sys.stdin = open('input.txt', 'rt') # read text

def dec_to_bin(x):
    if x//2 == 0:
        return str(1)

    else:
        c = x%2
        return dec_to_bin(x//2) + str(c)

n = int(input())

print(dec_to_bin(n))