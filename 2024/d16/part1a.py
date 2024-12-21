import math

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
TURN_COST = 1000

grid = []
start = None
end = None

with open('input.txt') as f:
  for row_idx, line in enumerate(f):
    if start is None:
      start_found = line.find('S')
      if (start_found != -1):
        start = (row_idx, start_found)
    if end is None:
      end_found = line.find('E')
      if (end_found != -1):
        end = (row_idx, end_found)
    grid.append([x == '#' for x in list(line.strip())])

def print_path(path):
  path_grid = []
  for row in grid:
    path_grid.append(['#' if x else '.' for x in row])
  for step in path:
    path_grid[step[0]][step[1]] == 'x'
  path_grid[start[0]][start[1]] == 'S'
  path_grid[end[0]][end[1]] == 'E'
  for row in path_grid:
    print(''.join(row))
  print("\n")

memo = {}

open('output.txt', 'w').close()
file = open('output.txt', 'a')
def search(current, direction, goal, seen_directions, path, cost):
  #print(f"current: {current}, path: {path}, cost: {cost}")
  file.write(f"current: {current}, path: {path}, cost: {cost}\n")
  if (current, direction) in memo:
    print("memo")
    return memo[((current, direction))]

  if (current[0] < 0) or (current[1] < 0) or (current[0] >= len(grid)) or (current[1] >= len(grid[0])):
    return math.inf

  if current in path:
    return math.inf
  
  if (direction in seen_directions) or (len(seen_directions) > 2):
    return math.inf

  # check for wall
  if grid[current[0]][current[1]]:
    return math.inf

  if direction in seen_directions:
    return math.inf

  if sum([int(grid[current[0] + neighbor[0]][current[1] + neighbor[1]]) for neighbor in DIRECTIONS]) > 2:
    return math.inf

  # check for goal
  if current == goal:
    #print(f"found goal! cost: {cost}\npath: {path}\n")
    #print_path(path)
    return cost
  
  # always try moving forwards
  results = [search((current[0] + DIRECTIONS[direction][0], current[1] + DIRECTIONS[direction][1]), direction, goal, set(), path + [current], cost + 1)]

  seen_directions.add(direction)
  if len(seen_directions) < 2:
    results.extend([
      search(current, (direction + 1) % 4, goal, seen_directions, path, cost + TURN_COST),
      search(current, (direction - 1) % 4, goal, seen_directions, path, cost + TURN_COST)
    ])

  memo[(current, direction)] = min(results)
  return min(results)

f.close()
print(search(start, 1, end, set(), [], 0))