# Uses python3

import sys
from itertools import chain

# assume starts = [0,7], ends = [5,10], points = [1,6,11]
def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    # list(a) = [(0,-inf),(8,-inf)]
    a = zip(starts, [float('-inf')]*len(starts))
    # list(b) = [(5, inf),(10,inf)]
    b = zip(ends, [float('inf')]*len(ends))
    # list(c) = [(1,0),(6,1),(11,2)]
    c = zip(points, range(len(points)))
    # sort a,b,c based on starts, ends, points
    sortedlist = sorted(chain(a,b,c), key=lambda a : (a[0], a[1]))
    stack = []
    for i, j in sortedlist:
        # add one element if it starts before the point
        if j == float('-inf'):
            stack.append(j)
        # remove one element if it ends before the point
        elif j == float('inf'):
            stack.pop()
        else:
            # j = 0, 1, 2
            cnt[j] = len(stack)
    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')