#Uses python3
def gcd(a, b):
    if b == 0:
        return a
    else:
        a_p = a % b
        return gcd(b, a_p)

def lcm(a, b):
    return (a * b) // gcd(a, b)

x, y = [int(x) for x in input("Enter two integers: ").split()]
print("LCM:", lcm(x, y))