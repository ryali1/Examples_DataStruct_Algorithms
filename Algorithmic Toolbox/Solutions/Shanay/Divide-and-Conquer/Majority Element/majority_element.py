# python3


def majority_element_naive(elements):
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0


def majority_element(elements):
    assert len(elements) <= 10 ** 5
    def majority_element_helper(elements):
        if len(elements) == 0:
            return 0
        if len(elements) == 1:
            return elements[0]
        midpoint = len(elements) // 2
        left = majority_element_helper(elements[0:midpoint])
        right = majority_element_helper(elements[midpoint:])
        if left == right:
            return left
        if elements.count(left) > midpoint:
            return left
        if elements.count(right) > midpoint:
            return right
        return None
    if majority_element_helper(elements) == None:
        return 0
    else:
        return 1

if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))
