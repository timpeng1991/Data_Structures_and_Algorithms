# Uses python3
def optimal_summands(k):
    summands = []
    l = 1
    while True:
        if k > 2 * l:
            summands.append(l)
            k -= l
            l += 1
        else:
            summands.append(k)
            return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x)

