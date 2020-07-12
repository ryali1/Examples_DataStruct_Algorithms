# python3

from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest


def largest_number(numbers):
    list1 = list()
    list1.append(numbers[0])
    list2 = list()
    z = 0
    s = ""
    for i in range(1, len(numbers)):
        for j in range(0, len(list1) + 1):
            list2 = list1.copy()
            list2.insert(j, numbers[i])
            if int(s.join(map(str, list2))) > z:
                z = int(s.join(map(str, list2)))
                counter = j
        list1.insert(counter, numbers[i])
    return int(s.join(map(str, list1)))


if __name__ == '__main__':
    n = int(input())
    input_numbers = input().split()
    assert len(input_numbers) == n
    print(largest_number(input_numbers))
