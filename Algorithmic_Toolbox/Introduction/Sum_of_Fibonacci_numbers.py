#Uses python3
def sum_fib(n):
    F = [0, 1]
    # the last digits of fib numbers occur in sequences of len 60
    for i in range(2, 60):
        F.append((F[i-1] + F[i-2]) % 10)
    if n < 60:
        return sum(F[: n+1]) % 10
    else:
        return (sum(F)*((n-m)//60) + sum(F[: (n+1) % 60])) % 10

x = input()
print sum_fib(x)