# python3


def max_pairwise_product_naive(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)

    product = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            product = max(product, numbers[i] * numbers[j])

    return product


def max_pairwise_product(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)
    index1 = 0
    maxnum1 = 0
    index2 = 0
    maxnum2 = 0
    for i in range(len(numbers)):
        maxnum1 = max(maxnum1, numbers[i])
    index1 = numbers.index(maxnum1)
    for j in range(len(numbers)):
        if j == index1:
            continue
        else:
            maxnum2 = max(maxnum2, numbers[j])
    index2 = numbers.index(maxnum2)

    product = maxnum1 * maxnum2
    return product


if __name__ == '__main__':
    n = int(input())
    input_numbers = list(map(int, input().split()))
    assert len(input_numbers) == n
    print(max_pairwise_product(input_numbers))
