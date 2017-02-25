# Uses python3
def get_change(m):
    n = 0
    for i in [10, 5, 1]:
        n += m//i
        m %= i
    return n

m = int(input())
print(get_change(m))