import os
from collections import defaultdict
from functools import reduce

with open(os.path.join("input.txt")) as f:
    data = f.read().splitlines()

def get_adjacent(x, y, cols, rows):
    return [(x + dx, y + dy) for dx in range(-1, 2) for dy in range(-1, 2)
            if (dx != 0 or dy != 0) and 0 <= x + dx < cols and 0 <= y + dy < rows]

rows, cols = len(data), len(data[0])
total = 0

d = defaultdict(list)

for y in range(rows):
    x = 0
    while x < cols:
        if data[y][x].isdigit():
            num, checks = data[y][x], get_adjacent(x, y, cols, rows)

            for i in range(x + 1, cols):
                if not data[y][i].isdigit():
                    break
                num += data[y][i]
                checks.extend(get_adjacent(i, y, cols, rows))
                x += 1

            for nx, ny in checks:
                if data[ny][nx] == "*":
                    d[(nx, ny)].append(int(num))
                    break
        x += 1

for nums in d.values():
    if len(nums) > 1:
        total += reduce(lambda a, b: a * b, nums)

print(total)