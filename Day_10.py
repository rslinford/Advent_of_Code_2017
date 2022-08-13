class Ring:
    def __init__(self, size):
        self.ring = [x for x in range(size)]
        self.current_pos = 0
        self.skip_size = 0

    def swap(self, i, j):
        temp = self.ring[i]
        self.ring[i] = self.ring[j]
        self.ring[j] = temp

    def __len__(self):
        return len(self.ring)

    def advance_current_pos(self, n):
        self.current_pos = (self.current_pos + n + self.skip_size) % len(self.ring)

    def increase_skip_size(self):
        self.skip_size += 1

    def __repr__(self):
        rval = []
        for i in range(len(self.ring)):
            if i > 0:
                rval.append(', ')
            if i == self.current_pos:
                rval.append('[')
            rval.append(str(self.ring[i]))
            if i == self.current_pos:
                rval.append(']')
        return ''.join(rval)

    def hash_value(self):
        return self.ring[0] * self.ring[1]


def read_puzzle_data(filename):
    with open(filename, 'r') as f:
        data = [int(x) for x in f.read().strip().split(',')]
    return data


def indexes_are_just_one_apart_or_less(i, j, ring_size):
    if i == j or abs(i - j) <= 1:
        return True
    if (i == 0 and j == ring_size - 1) or (i == ring_size - 1 and j == 0):
        return True
    return False

def hash(input, ring_size):
    ring = Ring(ring_size)
    for n in input:
        indexes_close_swap = 0
        i = ring.current_pos
        j = (ring.current_pos + n - 1) % len(ring)
        prev_ring = str(ring)
        while abs(i - j) > 0:
            if indexes_are_just_one_apart_or_less(i, j, len(ring)):
                indexes_close_swap += 1
            if indexes_close_swap >= 2:
                break
            ring.swap(i, j)
            i += 1
            if i >= len(ring):
                i = 0
            j -= 1
            if j < 0:
                j = len(ring) - 1
        ring.advance_current_pos(n)
        ring.increase_skip_size()
        print(f'{prev_ring} -> {ring}')
    return ring.hash_value()

def part_one(filename):
    input = read_puzzle_data(filename)
    answer = hash(input, 5)
    print(f'Answer {answer}')

# Wrong guess: 7425
part_one('Day_10_small_data.txt')
