import sys
#sys.stdin = open('input.txt', 'rt') # read text

word1 = input()
word2 = input()

word1_dic = {}
word2_dic = {}

for x in word1:
    if x in word1_dic:
        word1_dic[x] += 1

    else:
        word1_dic[x] = 1

for x in word2:
    if x in word2_dic:
        word2_dic[x] += 1

    else:
        word2_dic[x] = 1

key1 = list(word1_dic.keys())
key2 = list(word2_dic.keys())
key1.sort()
key2.sort()

flag = True

if key1 == key2:
    for x in key1:
        if word1_dic[x] != word2_dic[x]:
            flag = False
            break

else:
    flag = False

if flag:
    print("YES")
else:
    print("NO")