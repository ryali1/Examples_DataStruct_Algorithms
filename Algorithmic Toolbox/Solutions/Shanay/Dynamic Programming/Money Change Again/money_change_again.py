# python3


def change_naive(money):
    min_coins = float("inf")

    for num1 in range(money + 1):
        for num3 in range(money // 3 + 1):
            for num4 in range(money // 4 + 1):
                if 1 * num1 + 3 * num3 + 4 * num4 == money:
                    min_coins = min(min_coins, num1 + num3 + num4)

    return min_coins


def change(money):
    list1 = [money] * (money + 1)
    list1[0] = 0
    for i in range(1, money+1):
        a = i - 1
        b = i - 3
        c = i - 4
        if a >= 0 and b >= 0 and c >= 0:
            list1[i] = min(list1[i-1] + 1, list1[a] + 1, list1[b] + 1, list1[c] + 1)
        elif b < 0 and c < 0:
            list1[i] = min(list1[i-1] + 1, list1[a] + 1)
        else:
            list1[i] = min(list1[i-1] + 1, list1[a] + 1, list1[b] + 1)
    return list1[money]



if __name__ == '__main__':
    amount = int(input())
    print(change(amount))
