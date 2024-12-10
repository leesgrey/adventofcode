map = []
with open('input.txt') as f:
  for line in f:
    map.append([int(x) for x in list(line.strip())])

trailheads = []
for row_idx, row in enumerate(map):
  for col_idx, col in enumerate(row):
    if map[row_idx][col_idx] == 0:
      trailheads.append((row_idx, col_idx))

#print(trailheads)

def is_in_map(coords):
  return (coords[0] >= 0) and (coords[1] >= 0) and (coords[0] < len(map)) and (coords[1] < len(map[0]))

def leads_to_trail(coords, next, debug_path):
  if not is_in_map(coords):
    return []
  
  if map[coords[0]][coords[1]] != next:
    return []

  if next == 9:
    #print(f"trail {debug_path + [coords]} found")
    return [coords]
  
  return (leads_to_trail((coords[0] - 1, coords[1]), next + 1, debug_path + [coords])
        + leads_to_trail((coords[0], coords[1] + 1), next + 1, debug_path + [coords])
        + leads_to_trail((coords[0] + 1, coords[1]), next + 1, debug_path + [coords])
        + leads_to_trail((coords[0], coords[1] - 1), next + 1, debug_path + [coords]))

score = 0
for trailhead in trailheads:
  reached_nines = {}
  coords_to_check = leads_to_trail(trailhead, 0, [])
  for coord in coords_to_check:
    reached_nines[coord] = True
  
  score += len(reached_nines)
  #print(len(reached_nines))
print(f"score: {score}")