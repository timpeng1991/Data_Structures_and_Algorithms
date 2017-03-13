# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))
        # store the height of each node
        self.height = [0] * self.n

    def naive_compute_height(self):
        # a naive implementation
        maxHeight = 0
        for vertex in range(self.n):
            height = 0
            i = vertex
            while i != -1:
                height += 1
                i = self.parent[i]
            maxHeight = max(maxHeight, height)
        return maxHeight

    def compute_height(self, i):
        # use memoization to reduce running time
        # if the height of the i th node is already stored
        if self.height[i] != 0:
            return self.height[i]
        # if the i th node is the root
        if self.parent[i] == -1:
            self.height[i] = 1
            return self.height[i]
        # the height of the i th node is (1 + the height of its parent's height)
        self.height[i] = 1 + self.compute_height(self.parent[i])
        return self.height[i]

    def max_height(self):
        tree_height = 0
        for i in range(self.n):
            tree_height = max(tree_height, self.compute_height[i])
        return tree_height

def main():
  tree = TreeHeight()
  tree.read()
  print(tree.max_height())

threading.Thread(target=main).start()