# python3


def lcm_naive(a, b):
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9

    multiple = max(a, b)
    while multiple % a != 0 or multiple % b != 0:
        multiple += 1

    return multiple


def lcm(a, b):
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9

    multiplemax = (max(a, b))
    multiplemin = min(a,b)
    r = multiplemax
    for i in range(0, multiplemax):
        if r % multiplemin == 0:
            return r
        else:
            r = multiplemax * (i + 2)


if __name__ == '__main__':
    input_a, input_b = map(int, input().split())
    print(lcm(input_a, input_b))
