import re

robots = []

#DIMENSIONS = (11, 7)
DIMENSIONS = (101, 103)

#with open('sample.txt') as f:
with open('input.txt') as f:
  for line in f:
    match = re.findall("(-*[0-9]+),(-*[0-9]+)", line)
    position = [int(match[0][0]), int(match[0][1])]
    velocity = int(match[1][0]), int(match[1][1])
    robots.append((position, velocity))

def print_robot_grid(grid):
  for row in grid:
    string_rep = ""
    for val in row:
      if val == 0:
        string_rep += "."
      else:
        string_rep += str(val)
    print(string_rep)
  
def get_robot_grid():
  grid = [([0] * DIMENSIONS[0]) for _ in range(DIMENSIONS[1])]
  for robot in robots:
    position = robot[0]
    grid[position[1]][position[0]] += 1
  return grid

def move(robot, seconds=1):
  if (seconds == 0):
    return

  position = robot[0]
  velocity = robot[1]
  robot[0][0] = (position[0] + (velocity[0] * seconds)) % DIMENSIONS[0]
  robot[0][1] = (position[1] + (velocity[1] * seconds)) % DIMENSIONS[1]

current_time = 0
times_of_interest = []

print("finding points of interest")
for i in range(DIMENSIONS[0] * DIMENSIONS[1]):
  robots_with_neighbors = 0
  for robot in robots:
    move(robot)
  
  current_time += 1
  grid = get_robot_grid()
  for robot in robots:
    neighbors = 0
    position = robot[0]
    sides = [(position[0] - 1, position[1] + 0),
            (position[0] + 0, position[1] - 1),
            (position[0] + 0, position[1] + 1),
            (position[0] + 1, position[1] + 0)]
    for side in sides:
      if (side[0] > 0) and (side[1] > 0) and (side[0] < len(grid)) and (side[1] < len(grid[0])) and (grid[side[0]][side[1]] != 0):
        neighbors += 1
    if neighbors > 1:
      robots_with_neighbors += 1

  if robots_with_neighbors > 50:
    times_of_interest.append(current_time)

# reset
with open('input.txt') as f:
  for line in f:
    match = re.findall("(-*[0-9]+),(-*[0-9]+)", line)
    position = [int(match[0][0]), int(match[0][1])]
    velocity = int(match[1][0]), int(match[1][1])
    robots.append((position, velocity))
  
current_time = 0

for time in times_of_interest:
  print(f"time: {time}")
  for robot in robots:
    move(robot, (time - current_time))

  print_robot_grid(get_robot_grid())
