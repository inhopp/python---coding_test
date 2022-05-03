import sys
#sys.stdin = open('input.txt', 'rt') # read text

def DFS(elements):
    global count
    if len(elements) > m:
        return

    if len(elements) == m:
        count += 1
        for x in elements:
            print(x, end=" ")
        print()

    else:
        for i in range(n):
            DFS(elements + str(i+1))


           
n, m = map(int, input().split())
count = 0
DFS("")
print(count)