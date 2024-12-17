import math

TURN_COST = 1000
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

walls_grid = []
start = None
end = None

with open('sample.txt') as f:
    for row_idx, line in enumerate(f):
        for col_idx, spot in enumerate(line):
            if (start is None) and (spot == "S"):
                start = (row_idx, col_idx)
            elif (end is None) and (spot == "E"):
                end = (row_idx, col_idx)
        walls_grid.append([x == '#' for x in line.strip()])


def is_in_grid(coords):
    if (coords[0] < 0) or (coords[1] < 0) or (coords[0] >= len(walls_grid)) or (coords[1] >= len(walls_grid[1])):
        return False
    return True


def search(current, goal, facing, cost, path, seen_directions):
    print(f"\n{current}")
    print(path)
    print(seen_directions)
    if current == goal:
        print("yippee")
        return cost 
    
    if current in path:
        return math.inf

    if facing in seen_directions:
        return math.inf

    if not is_in_grid(current):
        return math.inf

    if walls_grid[current[0]][current[1]]:
        return math.inf

    updated_path = path.copy()
    updated_path.add(current)
    seen_directions.add(facing)
    
    # move forward, turn left, turn right
    return min(search((current[0] + DIRECTIONS[facing][0], current[1] + DIRECTIONS[facing][1]), goal, facing, cost + 1, updated_path, set()),
               search(current, goal, (facing + 1) % 4, cost + TURN_COST, path, seen_directions),
               search(current, goal, (facing - 1) % 4, cost + TURN_COST, path, seen_directions))

result = search(start, end, 1, 0, set(), set())
print(result)