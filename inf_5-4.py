import sys
#sys.stdin = open('input.txt', 'rt') # read text

s = input()
stack = []

for x in s:
    if x.isdecimal():
        stack.append(x)

    else:
        b = int(stack.pop())
        a = int(stack.pop())

        if x == '+':
            stack.append(a+b)
        elif x == '-':
            stack.append(a-b)
        elif x == '*':
            stack.append(a*b)
        else:
            stack.append(a/b)

print(stack[0])