# python3


def linear_search(keys, query):
    for i in range(len(keys)):
        if keys[i] == query:
            return i

    return -1


def binary_search(keys, query):

    assert 1 <= len(keys) <= 3 * 10 ** 4

    n = len(keys)
    minindex = 0
    maxindex = n-1
    while maxindex >= minindex:
        midindex = int(minindex + ((maxindex - minindex)/2))
        if keys[midindex] == query:
            return midindex
        elif keys[midindex] < query:
            minindex = midindex + 1
        else:
            maxindex = midindex - 1
    return -1


if __name__ == '__main__':
    input_keys = list(map(int, input().split()))[1:]
    input_queries = list(map(int, input().split()))[1:]

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
