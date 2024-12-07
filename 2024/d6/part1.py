grid = []
guard_pos = None
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
guard_facing = 0

with open('input.txt') as f:
  for line_idx, line in enumerate(f):
    col_idx = line.find("^")
    if col_idx != -1:
      guard_pos = [line_idx, col_idx]
    grid.append(list(line.strip()))

print(grid)
print(guard_pos)

left_map = False

while (not left_map):
  front = [guard_pos[0] + directions[guard_facing][0], guard_pos[1] + directions[guard_facing][1]]
  # if left map, stop
  if (front[0] < 0) or (front[1] < 0) or (front[0] >= len(grid)) or (front[1] >= len(grid[0])):
    print("left map")
    grid[guard_pos[0]][guard_pos[1]] = "X"
    left_map = True
    continue
  # if facing obstruction, turn
  elif grid[front[0]][front[1]] == "#":
    print("turning")
    guard_facing = (guard_facing + 1) % 4
  elif grid[front[0]][front[1]] != "#":
    grid[guard_pos[0]][guard_pos[1]] = "X"
    guard_pos = front
    print(guard_pos)
    front = [guard_pos[0] + directions[guard_facing][0], guard_pos[1] + directions[guard_facing][1]]

print(guard_pos)
sum = 0
for line in grid:
  for col in line:
    if col == "X":
      sum += 1
  print(line)
print(sum)