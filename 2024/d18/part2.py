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
    self.parent = parent
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

def find_path_with_bytes(byte_idx):
  fallen_bytes = falling_bytes[:byte_idx + 1]

  open = []
  heapq.heappush(open, Node(None, (0, 0)))
  closed = set()

  directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

  while len(open) > 0:
    current = heapq.heappop(open)
    #print(f"current: {current.position}, cost: {current.g}")
    closed.add(current)

    if current.position == exit:
      path = set()
      trace = current
      while trace is not None:
        path.add(trace.position)
        trace = trace.parent
      return path

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
  return None

best_path = set()

for byte_idx in range(len(falling_bytes)):
  new_byte = falling_bytes[byte_idx]
  print(f"\nbyte idx: {byte_idx}, {new_byte}")
  if (len(best_path) > 0) and (new_byte not in best_path):
    print("not in previous best path")
    continue
  else:
    print("previous best path interrupted, recalculating")
    best_path = find_path_with_bytes(byte_idx)
    if best_path is None:
      print(f"unreachable after block {new_byte}")
      break