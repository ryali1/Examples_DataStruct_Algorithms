# python3

from sys import stdin


def maximum_gold(capacity, weights):
    assert 1 <= capacity <= 10 ** 4
    assert 1 <= len(weights) <= 10 ** 3
    assert all(1 <= w <= 10 ** 5 for w in weights)
    x = len(weights) + 1
    y = capacity + 1
    arr = [[0]*y for _ in range(x)]
    for i in range(1, x):
        for j in range(1, y):
            arr[i][j] = arr[i-1][j]
            if weights[i-1] <= j:
                val = arr[i-1][j-weights[i-1]] + weights[i-1]
                if arr[i][j] < val:
                    arr[i][j] = val
    return arr[x-1][capacity]



if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
