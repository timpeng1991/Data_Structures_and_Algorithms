# Uses python3
# Modified from the merge sort algorithm
import sys

# returns the sorted array and the number of inversion pairs btw the two halves
def merge(a, b, left, right):
    # the first half and the second half of a are already sorted
    ave = (left + right) // 2
    # i is the index for the first half, j is the index for the second half
    i, j = left, ave
    # k is the index for b, which will store the sorted array in range(left, right)
    k = left
    count = 0
    # merge the two halves into b
    while i < ave and j < right:
        # if the element in the first half is smaller, just add it to b
        if a[i] <= a[j]:
            b[k] = a[i]
            i += 1
            k += 1
        # should count if the element in the second half is smaller
        else:
            b[k] = a[j]
            j += 1
            k += 1
            # since the first half is sorted, every element after the compared element
            # in the first half is bigger than this second half element
            count += ave - i
    # if no element left in the second half, put the rest of the first half in b
    while i < ave:
        b[k] = a[i]
        k += 1
        i += 1
    # if no element left in the first half, put the rest of the second half in b
    while j < right:
        b[k] = a[j]
        k += 1
        j += 1
    # copy and paste b to a, so that a is sorted in range(left, right)
    for i in range(left, right):
        a[i] = b[i]
    return count

# returns the sorted array and the number of inversions
def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    # add the number of inversions from each half
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    # add the number of inversions between two halves
    number_of_inversions += merge(a, b, left, right)
    return number_of_inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))