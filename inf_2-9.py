import sys
#sys.stdin = open('input.txt', 'rt') # read text

n = int(input())
reward = []

for i in range(n):
    numbers = list(map(int, input().split()))
    result = [0] * 6
    for j in range(3):
        result[numbers[j]-1] += 1

    if max(result) == 3:
        price = 10000 + ((result.index(3) + 1) * 1000)
        reward.append(price)

    elif max(result) == 2:
        price = 1000 + ((result.index(2) + 1) * 100)
        reward.append(price)

    else:
        for j in range(5, -1, -1):
            if result[j] == 1:
                price = (j+1)* 100
                reward.append(price)
                break

print(max(reward))