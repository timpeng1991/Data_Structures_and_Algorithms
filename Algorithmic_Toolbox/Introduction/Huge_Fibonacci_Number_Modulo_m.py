#Uses python3
def fib_mod(n, m):
    if n == 1:
        return 1
    # F is a list of Pisano period numbers
    F = [0, 1]
    for i in range(2, n+1):
        # this is the distributive property of modulo
        F.append((F[i-1] % m + F[i-2] % m) % m)
        # every new period starts with 01
        if F[i] == 1 and F[i-1] == 0:
            break
    # if n is larger than m, count the periods
    if n > m:
        period = len(F) - 2
        return F[n % period]
    # if n is smaller than m, there is no period
    else:
        return F[n]

# input and output
n, m = [int(x) for x in input().split()]
print(fib_mod(n, m))