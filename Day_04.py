def sort_letters_in_each_word(words):
    rval = []
    for word in words:
        w = [x for x in word]
        w.sort()
        w = ''.join(w)
        rval.append(w)
    return rval



def read_puzzle_data(filename):
    with open(filename, 'r') as f:
        rval = []
        data = f.read().strip().split('\n')
        for line in data:
            p = line.split(' ')
            p = sort_letters_in_each_word(p)
            p.sort()
            rval.append(p)
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

def part_two(filename):
    data = read_puzzle_data(filename)
    tally = 0
    for pass_phrase in data:
        if pass_phrase_is_valid(pass_phrase):
            tally += 1
    print(f'Valid pass phrases: {tally}')


part_two('Day_04_data.txt')