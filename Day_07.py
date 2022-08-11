import re


class LogEntry:
    instances = {}

    def __init__(self, program_name, weight):
        self.name = program_name
        self.weight = weight
        self.children = set()
        self.parent = None
        self.sibling_delta = 0
        LogEntry.instances[self.name] = self

    def __repr__(self):
        if self.parent:
            parent_name = self.parent.name
        else:
            parent_name = 'None'
        return f'LogEntry({self.name}, {self.weight}) parent: {parent_name} children: {self.children}'

    def __lt__(self, other):
        self.name < other.name

    def add_child(self, child):
        self.children.add(child)

    def total_weight(self):
        rval = self.weight
        for child_name in self.children:
            child = LogEntry.instances.get(child_name)
            rval += child.total_weight()
        return rval


def read_puzzle_data(filename):
    with open(filename, 'r') as f:
        data = [x.strip() for x in f.read().strip().split('\n')]
    rval = {}
    for line in data:
        result = re.search(r'^(\w+) \((\d+)\)', line)
        name = result.group(1)
        weight = int(result.group(2))
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


def total_weight_sort_key(entry):
    return entry.total_weight()

def one_of_these_things_is_not_like_the_other_children(log_entry):
    child_list = []
    for child in log_entry.children:
        child_entry = LogEntry.instances.get(child)
        child_list.append(child_entry)

    if len(child_list) < 3:
        # print(f'Warning: minimum of 3 children required. Found {len(child_list)} for {log_entry.name}')
        return None, 0
    child_list.sort(key=total_weight_sort_key, reverse=True)
    for x in child_list:
        print(f'Parent {log_entry.name}  Child {x.name}({x.weight})  total weight {x.total_weight()}')
    assert(child_list[0] != child_list[-1])
    delta = child_list[0].total_weight() - child_list[-1].total_weight()

    if child_list[0] == child_list[1]:
        return child_list[-1], delta
        child_list[-1].sibling_delta=delta
    else:
        child_list[0].sibling_delta=delta
        return child_list[0], delta

def follow_the_odd_one(log_entry):
    odd_child_entry, delta = one_of_these_things_is_not_like_the_other_children(log_entry)
    while odd_child_entry:
        prev_odd_child_entry = odd_child_entry
        odd_child_entry, delta = one_of_these_things_is_not_like_the_other_children(odd_child_entry)
        if not odd_child_entry:
            print(f'The node is {prev_odd_child_entry.parent.name}')
            return # todo: what should be returned here?
        if odd_child_entry:
            answer = prev_odd_child_entry.weight - prev_odd_child_entry.sibling_delta
            print(f'{odd_child_entry.name}({prev_odd_child_entry.weight}) is the odd ball for parent: {prev_odd_child_entry.name}  with a delta: {prev_odd_child_entry.sibling_delta} Answer: {answer}')
        else:
            print(f'Parent ({prev_odd_child_entry.name} has no odd children.')


def part_two(filename):
    log_entries = read_puzzle_data(filename)
    parentage(log_entries)
    root = pick_the_root(log_entries)
    follow_the_odd_one(root)


part_two('Day_07_data.txt')
