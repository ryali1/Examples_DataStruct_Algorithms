# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3
    a = money % 10
    b = money - a
    c = b/10
    d = a % 5
    if a < 5:
        e = 0
    else:
        e = 1
    total = c + d + e
    return int(total)



if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
