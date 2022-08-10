import unittest
from enum import Enum

import numpy as np

def pp(j, x, y):
    print(f'{j} ({x}, {y}) -> {abs(x) + abs(y)}')

class Direction(Enum):
    RIGHT = (0, 1)
    UP = (1, 0)
    LEFT = (0, -1)
    DOWN = (-1, 0)


def rotate(current_direction):
    match current_direction:
        case Direction.RIGHT:
            return Direction.UP
        case Direction.UP:
            return Direction.LEFT
        case Direction.LEFT:
            return Direction.DOWN
        case Direction.DOWN:
            return Direction.RIGHT



grid_size = 100001

def spiral(stop_at):
    grid = np.zeros((grid_size, grid_size), dtype=str)
    x_origen, y_origen = grid_size // 2, grid_size // 2
    x, y = x_origen, y_origen
    d = Direction.RIGHT
    i = 1
    n = 1
    grid[y][x] = n
    while True:
        for j in range(i):
            y += d.value[0]
            x += d.value[1]
            n += 1
            grid[y][x] = n
            if stop_at == n:
                return abs(y - y_origen) + abs(x - x_origen)
        match d:
            case Direction.RIGHT:
                pass
            case Direction.UP:
                i += 1
            case Direction.LEFT:
                pass
            case Direction.DOWN:
                i += 1
        d = rotate(d)




stop_at = 265149

print(f'The answer for {stop_at} is {spiral(stop_at)} ')

class TestSpiral(unittest.TestCase):
    def test_spiral(self):
        self.assertEqual(3, spiral(12))
        self.assertEqual(2, spiral(23))
        self.assertEqual(31, spiral(1024))
