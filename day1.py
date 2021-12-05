#!/usr/bin/env python3
import sys, utils

def find_sum(s, l):
    for v1 in l:
        for v2 in l:
            if v1 + v2 == s:
                return v1 * v2

def find_sum2(s, l):
    for v1 in l:
        for v2 in l:
            for v3 in l:
                if sum([v1, v2, v3]) == s:
                    return v1*v2*v3


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("please supply input file")
        sys.exit()

    l = utils.File(sys.argv[1]).get_ints()
    print(find_sum(2020, l))
    print(find_sum2(2020, l))



