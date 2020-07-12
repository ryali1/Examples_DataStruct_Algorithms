# python3


def fibonacci_number_naive(n):
    assert 0 <= n <= 45

    if n <= 1:
        return n

    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)


def fibonacci_number(n):
    assert 0 <= n <= 45
    total = n+1
    list1 = list()
    for i in range(0, total):
        if i <= 1:
            list1.append(i)
        else:
            list1.append(list1[i-1] + list1[i-2])
    return list1[n]

if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
