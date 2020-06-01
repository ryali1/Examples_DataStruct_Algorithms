# python3


def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current


def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    total = n+1
    list1 = list()
    for i in range(0, total):
        if i <= 1:
            list1.append(i)
        else:
            list1.append((list1[i-2] + list1[i-1]) % m)
        if i > 1 and list1[i-1] == 0 and list1[i] == 1:
            period = i-1
            remainder = n % period
            return list1[remainder]
        if i == n:
            return list1[n]



if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))




