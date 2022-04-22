import sys
#sys.stdin = open('input.txt', 'rt') # read text

card = [0] * 20
for i in range(20):
    card[i] = i+1

for i in range(10):
    a, b = map(int, input().split())
    list1 = card[:a-1]
    list2 = card[a-1:b]
    list3 = card[b:]
    reverse_list2 = list2[::-1]
    card = list1 + reverse_list2 + list3

for i in range(20):
    print(card[i], end=' ')