# python3


def find_maximum_value(dataset):
    assert 1 <= len(dataset) <= 29

    def minmax(i, j):
        n = int((len(dataset) - 1)/2)
        minimum = 10000000000000000000000000
        maximum = -10000000000000000000000000
        op = [0]*n
        for e in range(0, n):
            op[e] = dataset[2*e + 1]
        for k in range(i, j):
            if op[k] == "+":
                a = M[i][k] + M[k+1][j]
                b = M[i][k] + m[k+1][j]
                c = m[i][k] + M[k+1][j]
                d = m[i][k] + m[k+1][j]
                minimum = min(a, b, c, d, minimum)
                maximum = max(a, b, c, d, maximum)
            elif op[k] == "-":
                a = M[i][k] - M[k+1][j]
                b = M[i][k] - m[k+1][j]
                c = m[i][k] - M[k+1][j]
                d = m[i][k] - m[k+1][j]
                minimum = min(a, b, c, d, minimum)
                maximum = max(a, b, c, d, maximum)
            elif op[k] == "*":
                a = M[i][k] * M[k+1][j]
                b = M[i][k] * m[k+1][j]
                c = m[i][k] * M[k+1][j]
                d = m[i][k] * m[k+1][j]
                minimum = min(a, b, c, d, minimum)
                maximum = max(a, b, c, d, maximum)

        return minimum, maximum
    x = int((len(dataset) + 1)/2)
    num = [0]*x
    for y in range(0, x):
        num[y] = int(dataset[2*y])
    m = [[0]*x for _ in range(x)]
    M = [[0]*x for _ in range(x)]
    for z in range(0, x):
        m[z][z] = num[z]
        M[z][z] = num[z]
    for s in range(0, x-1):
        for t in range(0, x-s-1):
            u = t + s + 1
            m[t][u], M[t][u] = minmax(t, u)
    return M[0][z]


if __name__ == "__main__":
    print(find_maximum_value(input()))
