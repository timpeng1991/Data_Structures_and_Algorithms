#Uses python3
def par_sum(m, n):
    F = [0, 1]
    # the last digits of fib numbers occur in sequences of len 60
    for i in range(2, 60):
        F.append((F[i-1] + F[i-2]) % 10)
    # less than one period
    if n - m < 60:
        return sum(F[m: n+1]) % 10
    # more than one period
    else:
        return (sum(F)*((n-m)//60) + sum(F[(m % 60):(n % 60)+1])) % 10

m, n = [int(x) for x in input().split()]
print(par_sum(m, n))