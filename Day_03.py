import unittest
from enum import Enum

import numpy as np

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

def sum_adjacent_squares(grid, y, x):
    total = 0
    total += grid[y][x+1]
    total += grid[y+1][x+1]
    total += grid[y+1][x]
    total += grid[y+1][x-1]
    total += grid[y][x-1]
    total += grid[y-1][x-1]
    total += grid[y-1][x]
    total += grid[y-1][x+1]
    return total

grid_size = 10000

def spiral(stop_at):
    grid = np.zeros((grid_size, grid_size), dtype=np.ulonglong)
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
            grid[y][x] = sum_adjacent_squares(grid, y, x)
            if grid[y][x] > stop_at:
                return grid[y][x]
            # print(grid)
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
# stop_at = 100

print(f'The answer for {stop_at} is {spiral(stop_at)} ')
