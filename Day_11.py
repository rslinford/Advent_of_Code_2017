import unittest
from redblobgames import Hex, hex_neighbor, hex_distance


def read_puzzle_input(filename):
    with open(filename, 'r') as f:
        data = f.read().strip().split(',')
    return data


"""

  \ n  /
nw +--+ ne
  /    \
-+      +-
  \    /
sw +--+ se
  / s  \

"""

def part_one(filename):
    data = read_puzzle_input(filename)
    start_hex = Hex(0,0,0)
    h = start_hex
    for d in data:
        match d:
            case 'n':
                # print('North')
                h = hex_neighbor(h, 2)
            case 'ne':
                # print('North East')
                h = hex_neighbor(h, 1)
            case 'se':
                # print('South East')
                h = hex_neighbor(h, 0)
            case 's':
                # print('South')
                h = hex_neighbor(h, 5)
            case 'sw':
                # print('South West')
                h = hex_neighbor(h, 4)
            case 'nw':
                # print('North West')
                h = hex_neighbor(h, 3)
            case _:
                assert False
    distance = hex_distance(start_hex, h)
    return distance


def part_two(filename):
    data = read_puzzle_input(filename)
    start_hex = Hex(0,0,0)
    h = start_hex
    max_distance = 0
    for d in data:
        match d:
            case 'n':
                h = hex_neighbor(h, 2)
            case 'ne':
                h = hex_neighbor(h, 1)
            case 'se':
                h = hex_neighbor(h, 0)
            case 's':
                h = hex_neighbor(h, 5)
            case 'sw':
                h = hex_neighbor(h, 4)
            case 'nw':
                h = hex_neighbor(h, 3)
            case _:
                assert False
        distance = hex_distance(start_hex, h)
        if distance > max_distance:
            max_distance = distance
    return max_distance


class Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(877, part_one('Day_11_data.txt'))
        self.assertEqual(0, part_one('Day_11_test_01_data.txt'))
        self.assertEqual(3, part_one('Day_11_test_02_data.txt'))

    def test_part_two(self):
        self.assertEqual(-1, part_two('Day_11_data.txt'))
