DIRECTIONS = [
    (0, 1), # E
    (1, 1), # SE
    (1, 0), # S
    (1, -1), # SW
    (0, -1), # W
    (-1, -1), # NW
    (-1, 0), # N
    (-1, 1), # NE
]

grid = []
with open('input.txt') as f:
    for row in f:
        grid.append([1 if x == '@' else 0 for x in row])


def print_grid(grid):
    for line in grid:
        print(''.join(['@' if c else '.' for c in line]))


num_rows = len(grid)
num_cols = len(grid[0])


def is_roll(row, col) -> bool:
    if (row < 0 or col < 0 or row >= num_rows or col >= num_cols):
        return False
    return bool(grid[row][col])


def adjacent_rolls(row, col) -> int:
    total = 0
    for direction in DIRECTIONS:
        if is_roll(row + direction[0], col + direction[1]):
            total += 1

    return total

def forklift() -> int:
    forklifted = 0
    for row_idx in range(num_rows):
        for col_idx in range(num_cols):
            if is_roll(row_idx, col_idx) and adjacent_rolls(row_idx, col_idx) < 4:
                grid[row_idx][col_idx] = 0
                forklifted += 1
    
    return forklifted

forklifted = forklift()
total = forklifted
while (forklifted > 0):
    forklifted = forklift()
    total += forklifted

print(total)