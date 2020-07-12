# python3

from random import randint


def partition3(array, left, right):
    pivot = array[left]

    i = left
    j = right
    mid = left
    while mid <= j:
        if array[mid] < pivot:
            array[i], array[mid] = array[mid], array[i]
            i = i + 1
            mid = mid + 1
        elif array[mid] > pivot:
            array[mid], array[j] = array[j], array[mid]
            j = j - 1
        elif array[mid] == pivot:
            mid = mid + 1
    return i, j



def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    m1, m2 = partition3(array, left, right)
    randomized_quick_sort(array, left, m1 - 1)
    randomized_quick_sort(array, m2 + 1, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
