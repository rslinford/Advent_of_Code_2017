import queue


def load_puzzle_data(filename):
    with open(filename, 'r') as f:
        data = f.read().strip()
    return data


def parse_data(data):
    q = queue.LifoQueue()
    inside_garbage = False
    ignore_next_character = False
    depth = 0
    running_score = 0
    for c in data:
        if ignore_next_character:
            ignore_next_character = False
            continue
        if inside_garbage:
            match c:
                case '>':
                    pop_char = q.get()
                    assert (pop_char == '<')
                    inside_garbage = False
                case '!':  # ignore the next character
                    ignore_next_character = True
                case _:
                    pass # in garbage anything goes
            continue
        match c:
            case '{': # begin group
                q.put(c)
                depth += 1
                running_score += depth
                print(f'Begin group at depth {depth}')
            case '}': # end group
                pop_char = q.get()
                print(f'End group at depth {depth}')
                depth -= 1
                assert(pop_char == '{')
            case '<': # garbage begins
                q.put(c)
                inside_garbage = True
            case '!': # ignore the next character
                ignore_next_character = True
    print(f'Running score {running_score}')

def part_one(filename):
    data = load_puzzle_data(filename)
    parse_data(data)

part_one('Day_09_small_data.txt')
