#!/usr/bin/env python3
import sys, utils, re

class Passport(object):
    def __init__(self, d: dict):
        self.props = {
                'byr': '',
                'iyr': '', 
                'eyr': '',
                'hgt': '',
                'hcl': '',
                'ecl': '',
                'pid': '',
                'cid': '',
                }
        self._parse(d)

    def _parse(self, d):
        for k,v in d.items():
            if k == 'byr':
                self.props['byr'] = v
            if k == 'iyr':
                self.props['iyr'] = v
            if k == 'eyr':
                self.props['eyr'] = v
            if k == 'hgt':
                self.props['hgt'] = v
            if k == 'hcl':
                self.props['hcl'] = v
            if k == 'ecl':
                self.props['ecl'] = v
            if k == 'pid':
                self.props['pid'] = v
            if k == 'cid':
                self.props['cid'] = v

    def __str__(self):
        s = ''
        for k, v in self.props.items():
            s += f'{k}: \t{v}\n'
        return s

    def is_valid_no_cid(self):
        for k, v in self.props.items():
            if k == 'cid':
                continue
            if v == '':
                return False
        return True

    def is_valid(self):
        valid = True
        if not self.is_valid_no_cid():
            valid = False
        elif not 1920 <= int(self.props['byr']) <= 2002:
            valid = False
        elif not 2010 <= int(self.props['iyr']) <= 2020:
            valid = False
        elif not 2020 <= int(self.props['eyr']) <= 2030:
            valid = False
        elif not self._validate_hgt():
            valid = False
        elif not self._validate_hcl():
            valid = False
        elif not self.props['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            valid = False
        elif not (len(self.props['pid']) == 9 and (int(self.props['pid']) in range(1, 1000000000))):
            valid = False
        return valid

    def _validate_hcl(self):
        p = re.compile(r'#[0-9a-f]{6}')
        return p.fullmatch(self.props['hcl'])


    def _validate_hgt(self):
        v = self.props['hgt']
        if v.endswith('cm') and not 150 <=int(v.rstrip('cm')) <= 193:
            return False
        elif v.endswith('in') and not 59 <= int(v.rstrip('in')) <= 76:
            return False
        return True


def get_passports(inp):
    passports = []
    tmp = dict()
    for line in inp:
        if line == '':
            p = Passport(tmp)
            passports.append(p)
            tmp = dict()
        tmp.update(parse_line(line))
    p = Passport(tmp)
    passports.append(p)
    return passports

def count_valid_no_cid(psp):
    return sum([1 for p in psp if p.is_valid_no_cid()])

def count_valid(psp):
    return sum([1 for p in psp if p.is_valid()])
    
def parse_line(line):
    line = line.split()
    d = dict()
    for elem in line:
        k, v = elem.split(':')
        d[k] = v
    return d

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("please supply input file")
        sys.exit()

    l = utils.File(sys.argv[1]).get_strings()
    psp = get_passports(l)
    print(count_valid_no_cid(psp))
    print(count_valid(psp))



