import re
import heapq

#exit = (6, 6)
exit = (70, 70)

#limit = 12
limit = 1024

falling_bytes = []

with open('input.txt') as f:
  for line in f:
    coords = [int(x) for x in re.findall(r"\d+", line)]
    assert(len(coords) == 2)
    falling_bytes.append((coords[0], coords[1]))

class Node:
  def __init__(self, parent, position):
    self.position = position

    if (parent is None):
      self.g = 0
    else:
      self.g = parent.g + 1
    self.h = abs(exit[0] - self.position[0]) + abs(exit[1] - self.position[1])
    self.f = self.g + self.h

  def __eq__(self, other):
    return self.position == other.position
  
  def __lt__(self, other):
    return self.f < other.f

  def __hash__(self):
    return hash(self.position)

  def __repr__(self):
    return f"{self.position}"

fallen_bytes = set(falling_bytes[:limit])
assert(len(fallen_bytes) == limit)

open = []
heapq.heappush(open, Node(None, (0, 0)))
closed = set()

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

while len(open) > 0:
  current = heapq.heappop(open)
  #print(f"current: {current.position}, cost: {current.g}")
  closed.add(current)

  if current.position == exit:
    print(f"yippee - cost {current.g}")
    break

  for direction in directions:
    child = Node(current, (current.position[0] + direction[0], current.position[1] + direction[1]))

    # out of bounds
    if (child.position[0] < 0) or (child.position[1] < 0) or (child.position[0] > exit[0]) or (child.position[1] > exit[1]):
      continue

    # corrupted
    if (child.position in fallen_bytes):
      continue


    if (child in closed):
      continue

    for node in open:
      if (child == node) and (child.g > node.g):
        continue

    heapq.heappush(open, child)
  
  #time.sleep(1)