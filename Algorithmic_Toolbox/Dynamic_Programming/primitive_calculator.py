# Uses python3
import sys

def optimal_sequence(n):
    if n == 1:
        return [0]
    # initialization
    sequence = []
    count = [0] * (n + 1)
    count[2], count[3] = 1, 1
    # store the number of operations for each n
    for i in range(4, n + 1):
        a, b, c = float('inf'), float('inf'), count[i - 1]
        if i % 3 == 0:
            a = count[i // 3]
        if i % 2 == 0:
            b = count[i // 2]
        # C(n) = min{C(n/3)+1, C(n/2)+1, C(n-1)+1}
        count[i] = min(a, b, c) + 1
    # given the number of operations, return the sequence
    while n >= 1:
        sequence.append(n)
        a, b, c = float('inf'), float('inf'), count[n - 1]
        if n % 3 == 0:
            a = count[n // 3]
        if n % 2 == 0:
            b = count[n // 2]
        mi = min(a, b, c)
        if mi == a:
            n //= 3
        elif mi == b:
            n //= 2
        else:
            n -= 1
    return reversed(sequence)

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')