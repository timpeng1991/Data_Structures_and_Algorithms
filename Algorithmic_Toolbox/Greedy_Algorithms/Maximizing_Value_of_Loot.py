# Uses python3
def get_optimal_value(capacity, weights, values):
    value = 0.
    # value per weight
    vpw = []
    for i in range(len(weights)):
        vpw.append([float(values[i]/weights[i]), weights[i]])

    for i, w in sorted(vpw, key=lambda x: -x[0]):
        if capacity == 0:
            return value
        else:
            a = min(capacity, w)
            value += a * i
            capacity -= a
    return value

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
    
