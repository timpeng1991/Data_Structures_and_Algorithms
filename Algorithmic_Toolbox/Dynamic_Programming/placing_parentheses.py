# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

# the min and max value of the sub-expression from ith number to jth number
def MinAndMax(i, j, M, m, op):
    Min = float('inf')
    Max = float('-inf')
    # M(i, k), M(k+1, j)... should be already computed by solve in order of increasing (j - i)
    for k in range(i, j):
        # max(i, k) opk max(k+1, j)
        a = evalt(M[i][k], M[k + 1][j], op[k])
        # max(i, k) opk min(k+1, j)
        b = evalt(M[i][k], m[k + 1][j], op[k])
        # min(i, k) opk min(k+1, j)
        c = evalt(m[i][k], M[k + 1][j], op[k])
        # min(i, k) opk min(k+1, j)
        d = evalt(m[i][k], m[k + 1][j], op[k])
        Min = min(Min, a, b, c, d)
        Max = max(Max, a, b, c, d)
    return (Min, Max)

def get_maximum_value(dataset):
    op = dataset[1:len(dataset):2]
    number = dataset[0:len(dataset):2]
    n = len(number)
    # storing the max values for all sub-expressions
    M = [[0 for x in range(n)] for y in range(n)]
    # storing the min values for all sub-expressions
    m = [[0 for x in range(n)] for y in range(n)]
    # when j = i, sub-expression contains just one digit
    for i in range(n):
        m[i][i], M[i][i] = int(number[i]), int(number[i])
    # solve sub-problems in order of increasing s = (j - i), the difference btw i, j
    for s in range(1, n):
        for i in range(n - s):
            # j - i = s
            j = i + s
            m[i][j], M[i][j] = MinAndMax(i, j, M, m, op)
    return M[0][n - 1]

if __name__ == "__main__":
    print(get_maximum_value(input()))