import re

robots = []

# DIMENSIONS = (11, 7)
DIMENSIONS = (101, 103)

# with open('sample.txt') as f:
with open('input.txt') as f:
  for line in f:
    match = re.findall("(-*[0-9]+),(-*[0-9]+)", line)
    position = [int(match[0][0]), int(match[0][1])]
    velocity = int(match[1][0]), int(match[1][1])
    robots.append((position, velocity))

def print_robot_grid():
  print("\n")
  grid = [([0] * DIMENSIONS[0]) for _ in range(DIMENSIONS[1])]
  print(f"{len(grid[0])} x {len(grid)}")
  for robot in robots:
    position = robot[0]
    grid[position[1]][position[0]] += 1
  
  for row in grid:
    string_rep = ""
    for val in row:
      if val == 0:
        string_rep += "."
      else:
        string_rep += str(val)
    print(string_rep)

def move(robot, seconds=1):
  if (seconds == 0):
    return

  position = robot[0]
  velocity = robot[1]
  robot[0][0] = (position[0] + (velocity[0] * seconds)) % DIMENSIONS[0]
  robot[0][1] = (position[1] + (velocity[1] * seconds)) % DIMENSIONS[1]

for robot in robots:
  move(robot, 100)

quadrant_size = (DIMENSIONS[0] // 2, DIMENSIONS[1] // 2)
quadrants = {(0, 0): 0, (0, 1): 0, (1, 0): 0, (1, 1): 0}

for robot in robots:
  quadrant = [None, None]
  position = robot[0]
  if position[0] < quadrant_size[0]:
    quadrant[0] = 0
  elif position[0] > quadrant_size[0]:
    quadrant[0] = 1
  else:
    continue

  if position[1] < quadrant_size[1]:
    quadrant[1] = 0
  elif position[1] > quadrant_size[1]:
    quadrant[1] = 1
  else:
    continue

  quadrants[(quadrant[0], quadrant[1])] += 1

safety_factor = 1
for quadrant in quadrants:
  safety_factor *= quadrants[quadrant]

print(safety_factor)