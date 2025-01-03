grid = []
antennas = {}
antinodes = {}

with open('input.txt') as f:
  for row_idx, line in enumerate(f):
    for col_idx, char in enumerate(line.strip()):
      if char != ".":
        if char in antennas:
          antennas[char].append((row_idx, col_idx))
        else:
          antennas[char] = [(row_idx, col_idx)]
    grid.append(list(line.strip()))

def is_in_grid(pos):
  return (pos[0] >= 0) and (pos[0] < len(grid)) and (pos[1] >= 0) and (pos[1] < len(grid[0]))

for frequency in antennas:
  for idx, location in enumerate(antennas[frequency]):
    others = antennas[frequency][:idx] + antennas[frequency][idx + 1:]
    for other in others:
      to_other = (other[0] - location[0], other[1] - location[1])
      target_a = (location[0] + to_other[0], location[1] + to_other[1])
      while (is_in_grid(target_a)):
        antinodes[target_a] = True
        target_a = (target_a[0] + to_other[0], target_a[1] + to_other[1])
      target_b = (other[0] - to_other[0], other[1] - to_other[1])
      while (is_in_grid(target_b)):
        antinodes[target_b] = True
        target_b = (target_b[0] - to_other[0], target_b[1] - to_other[1])

print(len(antinodes))