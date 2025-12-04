grid = []
directions = [
    (0, 1), # E
    (1, 1), # SE
    (1, 0), # S
    (1, -1), # SW
    (0, -1), # W
    (-1, -1), # NW
    (-1, 0), # N
    (-1, 1), # NE
]

def print_grid(grid):
    for line in grid:
        print(''.join(['@' if c else '.' for c in line]))

with open('input.txt') as f:
    for row in f:
        grid.append([1 if x == '@' else 0 for x in row])

num_rows = len(grid)
num_cols = len(grid[0])

print_grid(grid)

def is_roll(row, col) -> bool:
    if (row < 0 or col < 0 or row >= num_rows or col >= num_cols):
        return False
    return bool(grid[row][col])

def adjacent_rolls(row, col) -> int:
    total = 0
    for direction in directions:
        if is_roll(row + direction[0], col + direction[1]):
            total += 1

    return total


forkliftable = 0
for row_idx in range(num_rows):
    for col_idx in range(num_cols):
        if is_roll(row_idx, col_idx) and adjacent_rolls(row_idx, col_idx) < 4:
            forkliftable += 1

print(forkliftable)