#!/usr/bin/env python3
import sys, utils

def password_valid(char, least, most, pwd):
    return pwd.count(char) in range(least, most+1)

def password_valid2(char, f, s, pwd):
    f, s = f-1, s-1
    if f >= len(pwd) or s >= len(pwd):
        return False
    elif pwd[f] == char and pwd[s] == char:
        return False
    return pwd[f] == char or pwd[s] == char

def parse_str(s):
    parts = s.split()
    least, most = (int(n) for n in parts[0].split('-'))
    char = parts[1].rstrip(':')
    return char, least, most, parts[2]

def solve(l):
    count = 0
    count2 = 0
    for line in l:
        char, least, most, pwd = parse_str(line)
        if password_valid(char, least, most, pwd):
            count += 1
        if password_valid2(char, least, most, pwd):
            count2 += 1
    return count, count2


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("please supply input file")
        sys.exit()

    l = utils.File(sys.argv[1]).get_strings()
    print(solve(l))



