lines = []
a_coords = []

with open('input.txt') as f:
  for row_idx, line in enumerate(f):
    lines.append(line[:-1])  # don't include newline
    for col_idx, char in enumerate(line):
      if char == "A":
        a_coords.append((row_idx, col_idx))

def check_for_xmas(a_coord):
  if (a_coord[0] == 0) or (a_coord[0] == len(lines) - 1) or (a_coord[1] == 0) or (a_coord[1] == len(lines[0]) - 1):
    return False

  if check_for_mas_a(a_coord) and check_for_mas_b(a_coord):
    return True

  return False

def check_for_mas_a(a_coord):
  val_a = lines[a_coord[0] - 1][a_coord[1] - 1]
  val_b = lines[a_coord[0] + 1][a_coord[1] + 1]
  if val_a == "M" and val_b == "S":
    return True
  elif val_a == "S" and val_b == "M":
    return True
  return False

def check_for_mas_b(a_coord):
  val_a = lines[a_coord[0] - 1][a_coord[1] + 1]
  val_b = lines[a_coord[0] + 1][a_coord[1] - 1]
  if val_a == "M" and val_b == "S":
    return True
  elif val_a == "S" and val_b == "M":
    return True
  return False

sum = 0
for a_coord in a_coords:
  sum += int(check_for_xmas(a_coord))

print(sum)
