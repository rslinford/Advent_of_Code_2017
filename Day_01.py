

def read_puzzle_data(filename):
    with open(filename, 'r') as f:
        data = f.read().strip()
    return data

def part_one(filename):
    digits = read_puzzle_data(filename)

    running_sum = 0
    for i in range(len(digits)-1):
        if digits[i] == digits[i+1]:
            running_sum += int(digits[i])
    if digits[0] == digits[-1]:
        running_sum += int(digits[0])
    return running_sum

def part_two(filename):
    digits = read_puzzle_data(filename)


print(f"The answer: {part_one('Day_01_data.txt')}")
