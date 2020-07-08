# python3


def last_digit_of_the_sum_of_fibonacci_numbers_again_naive(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    if to_index == 0:
        return 0

    fibonacci_numbers = [0] * (to_index + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, to_index + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers[from_index:to_index + 1]) % 10


def last_digit_of_the_sum_of_fibonacci_numbers_again(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    period = 60
    remainder1 = from_index % period
    if remainder1 == 0 or from_index <= 1:
        x = 0
    else:
        list1 = [0] * remainder1
        list1[1] = 1
        for i in range(2, remainder1):
            list1[i] = (list1[i-2] + list1[i-1])
        x = sum(list1) % 10

    remainder2 = to_index % period
    if remainder2 == 0:
        y = 0
    else:
        total2 = remainder2 + 1
        list2 = [0] * total2
        list2[1] = 1
        for j in range(2, total2):
            list2[j] = (list2[j-2] + list2[j-1])
        y = sum(list2) % 10

    remaining = y - x
    if remaining < 0:
        newremain = y + 10 - x
        return newremain
    else:
        return remaining



if __name__ == '__main__':
    input_from, input_to = map(int, input().split())
    print(last_digit_of_the_sum_of_fibonacci_numbers_again(input_from, input_to))
