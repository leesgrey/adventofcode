lines = []
x_coords = []

with open('input.txt') as f:
  for row_idx, line in enumerate(f):
    lines.append(line[:-1])  # don't include newline
    for col_idx, char in enumerate(line):
      if char == "X":
        x_coords.append((row_idx, col_idx))

def check_for_mas(remaining, dir, origin):
  if len(remaining) == 0:
    return True

  checking = (origin[0] + dir[0], origin[1] + dir[1])
  if (checking[0] < 0) or (checking[1] < 0) or (checking[0] >= len(lines)) or (checking[1] >= len(lines[0])):
    return False

  if lines[checking[0]][checking[1]] == remaining[0]:
    return check_for_mas(remaining[1:], dir, checking)
  else:
    return False

sum = 0
for x_coord in x_coords:
  sum += int(check_for_mas("MAS", (-1, 0), x_coord))
  sum += int(check_for_mas("MAS", (-1, 1), x_coord))
  sum += int(check_for_mas("MAS", (-1, -1), x_coord))
  sum += int(check_for_mas("MAS", (0, 1), x_coord))
  sum += int(check_for_mas("MAS", (0, -1), x_coord))
  sum += int(check_for_mas("MAS", (1, 0), x_coord))
  sum += int(check_for_mas("MAS", (1, 1), x_coord))
  sum += int(check_for_mas("MAS", (1, -1), x_coord))

print(sum)