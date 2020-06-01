# python3


def edit_distance(first_string, second_string):
    x = len(first_string)
    y = len(second_string)
    arr = [[0]*x for _ in range(y)]
    if first_string[0] == second_string[0]:
        arr[0][0] = 0
    else:
        arr[0][0] = 1
    for i in range(1, x):
        if first_string[i] == second_string[0]:
            arr[0][i] = arr[0][i-1]
        else:
            arr[0][i] = arr[0][i-1] + 1
    for j in range(1, y):
        if first_string[0] == second_string[j]:
            arr[j][0] = arr[j-1][0]
        else:
            arr[j][0] = arr[j-1][0] + 1
    for t in range(1, y):
        for s in range(1, x):
            if first_string[s] == second_string[t] and min(arr[t][s-1], arr[t-1][s], arr[t-1][s-1]) == arr[t-1][s-1]:
                arr[t][s] = arr[t-1][s-1]
            else:
                arr[t][s] = min(arr[t][s-1], arr[t-1][s], arr[t-1][s-1]) + 1
    return arr[y-1][x-1]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
