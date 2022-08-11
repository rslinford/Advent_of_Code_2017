import re


class LogEntry:
    def __init__(self, program_name, weight):
        self.name = program_name
        self.weight = weight
        self.children = set()
        self.parent = None
    def __repr__(self):
        if self.parent:
            parent_name = self.parent.name
        else:
            parent_name = 'None'
        return f'LogEntry({self.name}, {self.weight}) parent: {parent_name} children: {self.children}'

    def add_child(self, child):
        self.children.add(child)


def read_puzzle_data(filename):
    with open(filename, 'r') as f:
        data = [x.strip() for x in f.read().strip().split('\n')]
    rval = {}
    for line in data:
        result = re.search(r'^(\w+) \((\d+)\)', line)
        name = result.group(1)
        weight = result.group(2)
        entry = LogEntry(name, weight)
        rval[entry.name] = entry
        result = re.search(r'-> (.+)$', line)
        if result:
            children = result.group(1).strip().split(', ')
            for child in children:
                entry.add_child(child)
    return rval

def parentage(log_entries: dict):
    for entry in log_entries.values():
        if len(entry.children) == 0:
            continue
        for child in entry.children:
            child_entry = log_entries.get(child)
            child_entry.parent = entry


def pick_the_root(log_entries):
    for entry in log_entries.values():
        if not entry.parent:
            return entry


def part_one(filename):
    log_entries = read_puzzle_data(filename)
    parentage(log_entries)
    root = pick_the_root(log_entries)

    for entry in log_entries.values():
        print(entry)
    print(f'Root of tree {root}')


part_one('Day_07_small_data.txt')