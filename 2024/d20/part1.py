import heapq

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

grid = []
cheatable_walls = set()
start = None
end = None

with open('input.txt') as f:
  for row, line in enumerate(f):
    if start is None:
      search = line.find("S")
      if search != -1:
        start = (row, search)
    if end is None:
      search = line.find("E")
      if search != -1:
        end = (row, search)
    grid.append([x == "#" for x in line.strip()])

assert(start != -1)
assert(end != -1)

# get current optimal speed
class Node:
  def __init__(self, parent, position):
    self.position = position

    if parent is None:
      self.g = 0
    else:
      self.g = parent.g + 1
    self.h = abs(end[0] - self.position[0]) + abs(end[1] - self.position[1])
    self.f = self.g + self.h
  
  def __eq__(self, other):
    return self.position == other.position
  
  def __hash__(self):
    return hash(self.position)
  
  def __lt__(self, other):
    return self.f < other.f


def get_time(cheat=None, threshold=None):
  open = []
  heapq.heappush(open, Node(None, start))
  closed = set()

  while len(open) > 0:
    current = heapq.heappop(open)
    closed.add(current)

    if current.position == end:
      return current.g
    
    children = [Node(current, (current.position[0] + direction[0], current.position[1] + direction[1])) for direction in DIRECTIONS]
    for child in children:
      if child in closed:
        continue
      if not is_valid(child.position, cheat):
        continue
      if (threshold is not None) and (child.g > threshold):
        continue

      prune = False
      for node in open:
        if (node == child) and (child.g > node.g):
          prune = True
          continue
      if prune:
        continue

      heapq.heappush(open, child)

def is_valid(position, cheat=None):
  if (position[0] < 0) or (position[1] < 0) or (position[0] >= len(grid)) or (position[1] >= len(grid[0])):
    return False
  elif (grid[position[0]][position[1]]) and (position != cheat):
    return False
  return True


for row_idx, row in enumerate(grid):
  for col_idx, col in enumerate(row):
    if (is_valid((row_idx + 1, col_idx)) and is_valid((row_idx - 1, col_idx))) or (is_valid((row_idx, col_idx + 1)) and is_valid((row_idx, col_idx - 1))):
      cheatable_walls.add((row_idx, col_idx))

base_time = get_time()
print(f"base speed: {base_time}")

total = 0
for idx, wall in enumerate(cheatable_walls):
  print(f"cheat: {wall} ({idx}/{len(cheatable_walls)})")
  cheat_time = get_time(wall, base_time - 100)
  if cheat_time is None:
    continue
  #print(f"cheat {wall}: {cheat_time}s ({diff})")
  else:
    total += 1

print(total)