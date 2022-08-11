import re


class LogEntry:
    def __init__(self, program_name, weight):
        self.program_name = program_name
        self.weight = weight
        self.child_programs = set()
    def __repr__(self):
        return f'LogEntry({self.program_name}, {self.weight}) children: {self.child_programs}'

    def add_child(self, child):
        self.child_programs.add(child)


def read_puzzle_data(filename):
    with open(filename, 'r') as f:
        data = [x.strip() for x in f.read().strip().split('\n')]
    rval = []
    for line in data:
        result = re.search(r'^(\w+) \((\d+)\)', line)
        name = result.group(1)
        weight = result.group(2)
        entry = LogEntry(name, weight)
        rval.append(entry)
        result = re.search(r'-> (.+)$', line)
        if result:
            children = result.group(1).strip().split(', ')
            for child in children:
                entry.add_child(child)
    return rval


def part_one(filename):
    log = read_puzzle_data(filename)
    for entry in log:
        print(entry)


part_one('Day_07_small_data.txt')