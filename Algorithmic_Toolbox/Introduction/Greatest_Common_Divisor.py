#Uses python3
def gcd(a, b):
    if b == 0:
        return a
    else:
        a_p = a % b
        return gcd(b, a_p)

x, y = [int(x) for x in input("Enter two integers: ").split()]
print("GCD:", gcd(x, y))