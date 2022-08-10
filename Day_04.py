def read_puzzle_data(filename):
    with open(filename, 'r') as f:
        rval = []
        data = f.read().strip().split('\n')
        for line in data:
            l = line.split(' ')
            l.sort()
            rval.append(l)
    return rval

def pass_phrase_is_valid(pass_phrase):
    for i in range(len(pass_phrase) -1):
        if pass_phrase[i] == pass_phrase[i + 1]:
            return False
    return True


def part_one(filename):
    data = read_puzzle_data(filename)
    tally = 0
    for pass_phrase in data:
        if pass_phrase_is_valid(pass_phrase):
            tally += 1
    print(f'Valid pass phrases: {tally}')


part_one('Day_04_data.txt')