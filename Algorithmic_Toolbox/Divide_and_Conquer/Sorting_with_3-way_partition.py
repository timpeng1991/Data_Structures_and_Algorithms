# Uses python3
import sys
import random

# 3-way partition
def partition3(a, l, r):
    x = a[l]
    m1 = l
    m2 = r
    i = l + 1
    while i <= m2:
        if a[i] < x:
            # move it to the front, and increase the lower bound
            a[i], a[m1] = a[m1], a[i]
            # everything before m1 are smaller than the pivot element
            m1 += 1
            # increase the search index
            i += 1
        elif a[i] > x:
            # move it to the back, and reduce the upper bound
            a[i], a[m2] = a[m2], a[i]
            # everything after m2 are larger than the pivot element
            m2 -= 1
            # do not increase the search index here
            # because the swapped element (from the tail) has not been checked yet
        else:
            # everything between m1 and m2 are equal to the pivot element
            i += 1
    m = [m1, m2]
    return m

# 2-way partition
def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j

def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m = partition3(a, l, r)
    # if the case is [2,2,2,9,3], then m = [0, 2], m[0]-1 = -1
    randomized_quick_sort(a, l, max(m[0] - 1, l))
    # if the case is [1,1,2,2,2], then m = [2, 4], m[1]+1 = 5
    randomized_quick_sort(a, min(m[1] + 1, r), r)

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')