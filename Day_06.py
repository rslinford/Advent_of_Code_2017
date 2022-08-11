def read_puzzle_day(filename):
    with open(filename, 'r') as f:
        data = [int(x) for x in f.read().strip().split('\t')]
    return data

def part_one(filename):
    pattern_set = set()
    banks = read_puzzle_day(filename)
    completed_cycles = 0
    while True:
        max_value = max(banks)
        index = banks.index(max_value)
        banks[index] = 0
        for _ in range(max_value):
            index = (index + 1) % len(banks)
            banks[index] += 1
        pattern = ','.join([str(x) for x in banks])
        completed_cycles += 1
        if pattern in pattern_set:
            print(f'Done in {completed_cycles} redistribution cycles.')
            break
        pattern_set.add(pattern)


def part_two(filename):
    pattern_set = set()
    banks = read_puzzle_day(filename)
    cycle_detected = False
    pattern_flag = None
    completed_cycles = 0
    while True:
        max_value = max(banks)
        index = banks.index(max_value)
        banks[index] = 0
        for _ in range(max_value):
            index = (index + 1) % len(banks)
            banks[index] += 1
        pattern = ','.join([str(x) for x in banks])
        completed_cycles += 1
        if pattern in pattern_set and not cycle_detected:
            cycle_detected = True
            print(f'Cycle detected after {completed_cycles} redistribution cycles.')
            print(f'Resetting counter to zero.')
            completed_cycles = 0
            pattern_flag = pattern
        elif pattern == pattern_flag:
            print(f'One full revolution is {completed_cycles} redistribution cycles.')
            break
        pattern_set.add(pattern)




part_two('Day_06_data.txt')
