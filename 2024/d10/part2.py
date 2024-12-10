map = []
with open('sample.txt') as f:
  for line in f:
    map.append([int(x) for x in list(line.strip())])

trailheads = []
for row_idx, row in enumerate(map):
  for col_idx, col in enumerate(row):
    if map[row_idx][col_idx] == 0:
      trailheads.append((row_idx, col_idx))

print(trailheads)

def is_in_map(coords):
  return (coords[0] >= 0) and (coords[1] >= 0) and (coords[0] < len(map)) and (coords[1] < len(map[0]))

def number_of_trails(coords, next, debug_path):
  if not is_in_map(coords):
    return 0
  
  if map[coords[0]][coords[1]] != next:
    return 0

  if next == 9:
    #print(f"trail {debug_path + [coords]} found")
    return 1
  
  return (number_of_trails((coords[0] - 1, coords[1]), next + 1, debug_path + [coords])
        + number_of_trails((coords[0], coords[1] + 1), next + 1, debug_path + [coords])
        + number_of_trails((coords[0] + 1, coords[1]), next + 1, debug_path + [coords])
        + number_of_trails((coords[0], coords[1] - 1), next + 1, debug_path + [coords]))

score = 0
for trailhead in trailheads:
  reached_nines = {}
  num_trails = number_of_trails(trailhead, 0, [])
  print(num_trails)
  score += num_trails
print(f"score: {score}")