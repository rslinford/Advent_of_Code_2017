import queue
import unittest


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
    garbage_char_tally = 0
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
                    garbage_char_tally += 1 # in garbage anything goes
            continue
        match c:
            case '{': # begin group
                q.put(c)
                depth += 1
                running_score += depth
                # print(f'Begin group at depth {depth}')
            case '}': # end group
                pop_char = q.get()
                # print(f'End group at depth {depth}')
                depth -= 1
                assert(pop_char == '{')
            case '<': # garbage begins
                q.put(c)
                inside_garbage = True
            case '!': # ignore the next character
                ignore_next_character = True
    return running_score, garbage_char_tally

def part_one(filename):
    data = load_puzzle_data(filename)
    running_score, garbage_char_tally = parse_data(data)
    print(f'Running score {running_score}')

def part_two(filename):
    data = load_puzzle_data(filename)
    running_score, garbage_char_tally = parse_data(data)
    print(f'Running score {running_score}  garbage char tally {garbage_char_tally}')


part_two('Day_09_data.txt')

class TestParser(unittest.TestCase):
    def test_part_one(self):
        running_score, garbage_char_tally = parse_data('{{<!!>},{<!!>},{<!!>},{<!!>}}')
        self.assertEqual(9, running_score)
        running_score, garbage_char_tally = parse_data('{{<a!>},{<a!>},{<a!>},{<ab>}}')
        self.assertEqual(3, running_score)
        running_score, garbage_char_tally = parse_data('{{{},{},{{}}}}')
        self.assertEqual(16, running_score)

    def test_part_two(self):
        running_score, garbage_char_tally = parse_data('<{o"i!a,<{i<a>')
        self.assertEqual(10, garbage_char_tally)
        running_score, garbage_char_tally = parse_data('<!!!>>')
        self.assertEqual(0, garbage_char_tally)
        running_score, garbage_char_tally = parse_data('<random characters>')
        self.assertEqual(17, garbage_char_tally)

