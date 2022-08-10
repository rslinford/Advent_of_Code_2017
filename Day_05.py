def load_puzzle_data(filename):
    with open(filename, 'r') as f:
        data = [int(x) for x in f.read().strip().split('\n')]
        print(data)
    return data


def follow(instructions):
    ic = 0
    move_counter = 0
    while True:
        try:
            prev_ic = ic
            ic += instructions[ic]
            if instructions[prev_ic] >= 3:
                instructions[prev_ic] -= 1
            else:
                instructions[prev_ic] += 1
            move_counter += 1
        except IndexError:
            print(f"We've escaped in {move_counter} moves.")
            break


def part_one(filename):
    instructions = load_puzzle_data(filename)
    follow(instructions)


part_one('Day_05_data.txt')
