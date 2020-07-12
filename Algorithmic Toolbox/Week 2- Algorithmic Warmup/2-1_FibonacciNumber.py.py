# python3


def fibonacci_number_naive(n):
    assert 0 <= n <= 45

    if n <= 1:
        return n

    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)



def fibonacci_number(n):
    assert 0 <= n <= 45
    if n <= 1:
        return n
    last = 0
    pres = 1

    for i in range(1,n,1):
        last = pres
        pres = last+pres
    return pres



if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
