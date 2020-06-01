# python3


def compute_optimal_summands(n):
    assert 1 <= n <= 10 ** 9
    summands = []

    list1 = list()
    a = 0
    for i in range(0,n):
        list1.append(a + 1)
        a = a + 1
        if sum(list1) + a >= n:
            list1[i] = list1[i] + (n - sum(list1))
            return list1




    return summands


if __name__ == '__main__':
    input_n = int(input())
    output_summands = compute_optimal_summands(input_n)
    print(len(output_summands))
    print(*output_summands)
