# python3

from sys import stdin


def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    totalweightremaining = capacity
    totalvalue = 0
    maxprice1 = list()
    maxpos1 = list()
    unitprice = list()

    for i in range (0, len(prices)):
        unitprice.append(prices[i]/weights[i])

    for i in range(0,2 * 10 ** 6):

        maxprice1.append(max(unitprice))
        maxpos1.append(unitprice.index(max(unitprice)))
        if maxprice1[i] == 0:
            return totalvalue
        if weights[maxpos1[i]] >= totalweightremaining:
            totalvalue = totalvalue + (totalweightremaining * maxprice1[i])
            totalweightremaining = 0
            return totalvalue
        else:
            totalvalue = totalvalue + (weights[maxpos1[i]] * maxprice1[i])
            totalweightremaining = totalweightremaining - weights[maxpos1[i]]
            weights[maxpos1[i]] = 0
            unitprice[maxpos1[i]] = 0



if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print("{:.10f}".format(opt_value))
