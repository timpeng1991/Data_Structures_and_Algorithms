#Uses python3
import sys
import math

def sort_list(x, y):
    # sort the points based on x value
    m = []
    for i in range(len(x)):
        m.append([x[i], y[i]])
    m.sort(key=lambda x: x[1])
    for i in range(len(x)):
        x[i] = m[i][0]
        y[i] = m[i][1]

def minimum_distance(x, y):
    # return distance if two points left
    if len(x) == 2:
        dist = ((x[0]-x[1]) ^ 2 + (y[0]-y[1]) ^ 2) ^ (1/2)
        return dist
    # divide and conquer
    mid = len(x) // 2
    d1 = minimum_distance(x[:mid], y[:mid])
    d2 = minimum_distance(x[mid:], y[mid:])
    delta = min(d1, d2)
    # check if the points btw two segments have smaller distance
    temp = []
    # points btw (x[mid]-delta, x[mid]+delta)
    for i in range(len(x)):
        if x[i] > x[mid] + delta:
            break
        if x[i] >= x[mid] - delta:
            temp.append([x[i], y[i]])
    # points with y distance smaller than delta


    return dist

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    # get every other item, starting with the second
    x = data[1::2]
    # get every other item, starting with the third
    y = data[2::2]
    sort_list(x, y)
    print("{0:.9f}".format(minimum_distance(x, y)))