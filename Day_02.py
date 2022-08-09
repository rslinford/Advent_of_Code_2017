

def read_puzzle_data(filename):
    rval = []
    with open(filename, 'r') as f:
        for line in f:
            row = []
            rval.append(row)
            line = line.strip()
            line = line.split('\t')
            for x in line:
                row.append(int(x))

    return rval

def part_one(filename):
    sheet = read_puzzle_data(filename)
    tally = 0
    for row in sheet:
        tally += max(row) - min(row)
    return tally


def find_the_two_numbers_and_divide_them(row):
    for i, p in enumerate(row):
        for j, q in enumerate(row):
            if i == j:
                continue
            if p % q == 0:
                return p // q
    return None



def part_two(filename):
    sheet = read_puzzle_data(filename)
    tally = 0
    for row in sheet:
        tally += find_the_two_numbers_and_divide_them(row)
    return tally


print(f"The answer: {part_two('Day_02_data.txt')}")
