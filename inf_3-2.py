import sys
#sys.stdin = open('input.txt', 'rt') # read text

str_input = input()
str_num = ""

for i in range(len(str_input)):
    if str_input[i] >= '0' and str_input[i] <= '9':
        str_num += str_input[i]

num = int(str_num)
cnt = 0
for i in range(1, num+1):
    if num % i == 0:
        cnt += 1

print(num)
print(cnt)