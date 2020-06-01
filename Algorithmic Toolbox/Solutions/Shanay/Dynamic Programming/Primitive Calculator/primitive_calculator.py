# python3


def compute_operations(n):
    assert 1 <= n <= 10 ** 6
    list1 = [n] * n
    list2 = list()
    list1[0] = 0
    x = n
    list2.append(n)
    for i in range(1, n):
        a = (i+1) - 1
        if (i+1) % 2 == 0 and (i+1) % 3 == 0:
            b = int(((i+1) / 2) - 1)
            c = int(((i+1) / 3) - 1)
            list1[i] = min(list1[i-1] + 1, list1[a] + 1, list1[b] + 1, list1[c] + 1 )
        elif (i+1) % 2 == 0 and (i+1) % 3 != 0:
            b = int(((i+1) / 2) - 1)
            list1[i] = min(list1[i-1] + 1, list1[a] + 1, list1[b] + 1)
        elif (i+1) % 2 != 0 and (i+1) % 3 == 0:
            c = int(((i+1) / 3) - 1)
            list1[i] = min(list1[i-1] + 1, list1[a] + 1, list1[c] + 1)
        else:
            list1[i] = min(list1[i-1] + 1, list1[a] + 1)
    while x > 1:
        if list1[x-1] - list1[x-2] == 1:
            list2.insert(0, x-1)
            x = x-1
        elif x % 2 == 0 and list1[x-1] - list1[int((x/2)) - 1] == 1:
            list2.insert(0, int(x/2))
            x = int(x/2)
        elif x % 3 == 0 and list1[x-1] - list1[int((x/3)) - 1] == 1:
            list2.insert(0, int(x/3))
            x = int(x/3)
    return list2


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
