import sys
#sys.stdin = open('input.txt', 'rt') # read text

s = input()
stack = []
result = []

for x in s:
    if x.isdecimal():
        result.append(x)

    else:
        if x=='(':
            stack.append(x)

        elif x=='*' or x=='/':
            while stack and (stack[-1]=='*' or stack[-1]=='/'):
                result.append(stack.pop())
            stack.append(x)

        elif x=='+' or x=='-':
            while stack and stack[-1]!='(':
                result.append(stack.pop())
            stack.append(x)

        else:
            while stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()

while stack:
    result.append(stack.pop())

for x in result:
    print(x, end='')
print()