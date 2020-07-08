# python3


def last_digit_of_the_sum_of_squares_of_fibonacci_numbers_naive(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n

    fibonacci_numbers = [0] * (n + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, n + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum([f ** 2 for f in fibonacci_numbers]) % 10


def last_digit_of_the_sum_of_squares_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18

    period = 60
    remainder = n % period
    total = remainder + 1
    list1 = [0] * total
    if n <= 1:
        return n
    if remainder == 0:
        return 0
    list1[1] = 1
    for i in range(2, total):
        list1[i] = ((list1[i-2] + list1[i-1]) % 10)
    x = list1[remainder]
    y = list1[remainder-1]
    u = (x+y) % 10
    z = (u * x) % 10
    return z


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_the_sum_of_squares_of_fibonacci_numbers(input_n))
