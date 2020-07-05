import math

cash = int(input())
portions = [1, 3, 4]
coins = [0]+[math.inf]*cash

for i in range(1, cash+1):
    for j in portions:
        if i>=j:
            amount = coins[i-j]+1
            if amount < coins[i]:
                coins[i]= amount
print(coins[cash])


