#Uses python3

import sys

def lcs3(a, b, c):
    # 3-dimensional
    M = [[[0 for x in range(cn + 1)] for y in range(bn + 1)] for z in range(an + 1)]
    for k in range(cn + 1):
        for j in range(bn + 1):
            for i in range(an + 1):
                if i == 0 or j == 0 or k == 0:
                    M[i][j][k] = 0
                else:
                    x1 = M[i-1][j][k]
                    x2 = M[i][j-1][k]
                    x3 = M[i][j][k-1]
                    x4 = M[i-1][j-1][k]
                    x5 = M[i-1][j][k-1]
                    x6 = M[i][j-1][k-1]
                    x7 = M[i-1][j-1][k-1]
                    # if the three sequences match
                    x8 = M[i-1][j-1][k-1] + 1
                    if a[i-1] == b[j-1] == c[k-1]:
                        M[i][j][k] = max(x1, x2, x3, x4, x5, x6, x8)
                    else:
                        M[i][j][k] = max(x1, x2, x3, x4, x5, x6, x7)
    return M[an][bn][cn]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))