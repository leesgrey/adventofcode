import heapq

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

class Node:
  def __init__(self, parent, position, direction):
    self.position = position
    self.direction = direction

    if (parent is None):
      self.g = 0
    else:
      if parent.direction == self.direction:
        self.g = parent.g + 1
      else:
        self.g = parent.g + TURN_COST

    self.h = abs(end[0] - position[0]) + abs(end[1] - position[1])
    self.f = self.g + self.h
  
  def __eq__(self, other):
    return (self.position == other.position) and (self.direction == other.direction)
  
  def __lt__(self, other):
    return self.f < other.f

  def __hash__(self):
    return hash((self.position, self.direction))

  def __repr__(self):
    return f"Node(position={self.position} direction={self.direction})"

open = []
heapq.heappush(open, Node(None, start, 1))
closed = set()

while len(open) > 0:
  current_node = heapq.heappop(open)
  #print(current_node.g)
  closed.add(current_node)

  if current_node.position == end:
    print(f"yippee - cost {current_node.g}")
    break

  children = [Node(current_node,
                   (current_node.position[0] + DIRECTIONS[current_node.direction][0], current_node.position[1] + DIRECTIONS[current_node.direction][1]),
                   current_node.direction),
              Node(current_node,
                   current_node.position,
                   (current_node.direction + 1) % 4),
              Node(current_node,
                   current_node.position,
                   (current_node.direction - 1) % 4)]

  for child in children:
    if grid[child.position[0]][child.position[1]]:
      continue

    if child in closed:
      continue

    for node in open:
      if (child == node) and (child.g > node.g):
        continue
    
    heapq.heappush(open, child)
    