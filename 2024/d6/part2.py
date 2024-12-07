DIRECTIONS = [[-1, 0], [0, 1], [1, 0], [0, -1]]

grid = []
start_pos = None
guard_pos = None
guard_facing = 0

with open('input.txt') as f:
  for line_idx, line in enumerate(f):
    col_idx = line.find("^")
    if col_idx != -1:
      start_pos = [line_idx, col_idx]
    grid.append(list(line.strip()))

left_map = False
guard_pos = start_pos

def check_loop(obstacle_pos):
  #print("checking obstacle at " + str(obstacle_pos))
  seen = {}
  guard_facing = 0
  guard_pos = start_pos
  left_map = None

  while (not left_map):
    #print(seen)
    # print(str(guard_pos) + ", " + str(guard_facing))
    if ((guard_pos[0], guard_pos[1]) in seen):
      if (guard_facing in seen[(guard_pos[0], guard_pos[1])]):
        #print(obstacle_pos)
        return True
      seen[(guard_pos[0], guard_pos[1])].append(guard_facing)
    else:
      seen[(guard_pos[0], guard_pos[1])] = [guard_facing]

    front_pos = [guard_pos[0] + DIRECTIONS[guard_facing][0], guard_pos[1] + DIRECTIONS[guard_facing][1]]
    if (front_pos[0] < 0) or (front_pos[1] < 0) or (front_pos[0] >= len(grid)) or (front_pos[1] >= len(grid[0])):
      #print("left map")
      left_map = True
      continue
    elif (front_pos[0] == obstacle_pos[0] and front_pos[1] == obstacle_pos[1]) or (grid[front_pos[0]][front_pos[1]]) == "#":
      #print("turning")
      guard_facing = (guard_facing + 1) % 4
    else:
      grid[guard_pos[0]][guard_pos[1]] = "X"
      guard_pos = front_pos
      #print(guard_pos)
    
  return False

sum = 0
obstacles = {}
while (not left_map):
  #print(guard_pos)
  front_pos = [guard_pos[0] + DIRECTIONS[guard_facing][0], guard_pos[1] + DIRECTIONS[guard_facing][1]]
  if (front_pos[0] < 0) or (front_pos[1] < 0) or (front_pos[0] >= len(grid)) or (front_pos[1] >= len(grid[0])):
    #print("left map")
    left_map = True
    continue
  elif grid[front_pos[0]][front_pos[1]] == "#":
    #print("turning")
    guard_facing = (guard_facing + 1) % 4
  else:
    if (front_pos[0], front_pos[1]) not in obstacles:
      if check_loop(front_pos):
        obstacles[(front_pos[0], front_pos[1])] = True
        sum += 1
    guard_pos = front_pos
    #print(guard_pos)

print(sum)