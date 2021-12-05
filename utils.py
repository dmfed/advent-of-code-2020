class File(object):
    def __init__(self, filename):
        self.filename = filename
        self.lines = list()
        self._get_lines()

    def _get_lines(self):
        with open(self.filename, 'r') as f:
            for line in f:
                self.lines.append(line.rstrip('\n'))

    def get_strings(self) -> list:
        if not self.lines:
            return []
        return self.lines[:]

    def get_ints(self) -> list:
        if not self.lines:
            return []
        return [int(n) for n in self.lines]

    def get_line(self, n) -> str:
        return self.lines[n]

    def get_coords(self) -> list:
        pairs = [line.split(' -> ') for line in self.lines]
        for i in range(len(pairs)):
            pairs[i] = tuple(int(n) for n in pairs[i][0].split(',')) + tuple(int(n) for n in pairs[i][1].split(',')) 
        return pairs

    def close(self):
        self.lines = []
        self.filename = ''

    def len(self):
        return len(self.lines)

