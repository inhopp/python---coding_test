import sys
#sys.stdin = open('input.txt', 'rt') # read text

input_data = input()
input_data = list(input_data)
stack = []
count = 0

for i in range(len(input_data)):
    if input_data[i] == '(':
        stack.append('(')

    else:
        if input_data[i-1] == '(':
            stack.pop()
            count += len(stack)
        else:
            stack.pop()
            count += 1

print(count)