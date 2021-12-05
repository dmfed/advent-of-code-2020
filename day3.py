#!/usr/bin/env python3
import sys, utils

TREE = '#'
EMPTY = '.'

class Map(object):
    def __init__(self, starting):
        self.slope = starting
        self._expand()

    def _expand(self):
        while len(self.slope) > len(self.slope[0])/7:
            for i in range(len(self.slope)):
                self.slope[i].extend(self.slope[i])
                
    def get(self, y, x):
        return self.slope[y][x]

    def size(self):
        return len(self.slope), len(self.slope[0])

    def height(self):
        return len(self.slope)

def solve(forward, down, l):
    sl = l[:]
    for i in range(len(sl)):
        sl[i] = list(sl[i])
    m = Map(sl)
    count_trees = 0
    y = 0
    x = 0
    while y < m.height():
        if m.get(y, x) == TREE:
            count_trees += 1
        y += down
        x += forward 
    return count_trees

def solve2(l):
    slopes = [(1,1), (3, 1), (5, 1), (7, 1), (1, 2)]
    count = 1
    for s in slopes:
        f, d = s
        count *= solve(f, d, l)
    return count


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("please supply input file")
        sys.exit()

    l = utils.File(sys.argv[1]).get_strings()
    print(solve(3, 1, l))
    print(solve2(l))



