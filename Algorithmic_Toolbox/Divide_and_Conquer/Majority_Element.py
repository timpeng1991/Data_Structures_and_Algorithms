# Uses python3
import sys

def get_majority_element(a, left, right):
    # check the boundaries
    print(a[left:right], 'left limit:', left, 'right limit:', right)
    # what's the point of these two lines?
    if left == right:
        return -1
    # if only one element, itself is the majority element
    if left + 1 == right:
        return a[left]
    # cut the array into two halves (recursive)
    # the majority element is at least also the majority element of one of them
    k = (right - left) // 2
    L = get_majority_element(a, left, left+k)
    R = get_majority_element(a, left+k, right)
    # the only candidates of majority element in the array[left:right] are L and R
    count_l = 0
    count_r = 0
    # count the number of L and R in the array[left:right]
    # if their value is -1, then it's not a candidate
    if L != -1:
        for i in range(left, right):
            if a[i] == L:
                count_l += 1
    if R != -1:
        for j in range(left, right):
            if a[j] == R:
                count_r += 1
    # check the value of L and R, and their counts
    print('L num:', L, 'count l:', count_l, 'R num:', R, 'count r:', count_r)
    # check if the element appears more than n/2 times
    # if true, then it's a candidate of the majority element for the bigger array
    if count_l > (right - left) / 2:
        return L
    elif count_r > (right - left) / 2:
        return R
    else:
        return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
