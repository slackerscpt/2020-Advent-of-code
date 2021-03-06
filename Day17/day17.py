from collections import defaultdict
#https://www.geeksforgeeks.org/python-itertools-product/ 
#To understand product
from itertools import product

with open('input.txt', 'r') as file:
    data = file.read()


def parse_input(data):
    return [list(line) for line in data.split('\n')]


data = parse_input(data)


def find_active(data, dim=3):
    active = set()
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == '#':
                active.add((i, j, *([0]*(dim-2))))
    return active


def find_neighbors(active, dim=3):
    neighbors = defaultdict(int)
    for cube in active:
        for delta in product([-1, 0, 1], repeat=dim):
            if all(x == 0 for x in delta):
                continue
            cur = tuple(x+dx for x, dx in zip(cube, delta))
            neighbors[cur] += 1
    return neighbors


def step(active, dim=3):
    new_active = set()
    neighbors = find_neighbors(active, dim)
    for k, v in neighbors.items():
        if v == 3 or (v == 2 and k in active):
            new_active.add(k)
    return new_active


def part_one(data):
    active = find_active(data, 3)
    for _ in range(6):
        active = step(active, 3)
    return len(active)


def part_two(data):
    active = find_active(data, 4)
    for _ in range(6):
        active = step(active, 4)
    return len(active)

answer = part_one(data)
#print (answer)
print(f'Part 1: {part_one(data)}')  # 252
print(f'Part 2: {part_two(data)}')  # 2160