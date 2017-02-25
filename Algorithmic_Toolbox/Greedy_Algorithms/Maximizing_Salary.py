# Uses python3
# Compare the two possible combinations btw two number
def igoe(x, y):
    A = int(str(x) + str(y))
    B = int(str(y) + str(x))
    if A >= B:
        return True
    else:
        return False

def largest_number(a):
    res = ""
    while a:
        max_digit = 0
        # find the number which should be the first
        for d in a:
            # updated
            if igoe(d, max_digit):
            #if d >= max_digit:
                max_digit = d
        res += str(max_digit)
        a.remove(max_digit)
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
