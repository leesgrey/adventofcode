towels = None
designs = []

with open('input.txt') as f:
  reading_designs = False
  for line in f:
    if len(line.strip()) == 0:
      reading_designs = True
      continue

    if reading_designs:
      designs.append(line.strip())
    else:
      towels = line.strip().split(', ')

memo = {}

def num_arrangements(design):
  if design in memo:
    return memo[design]
  
  result = 0
  remaining = []
  for towel in towels:
    if design == towel:
      result += 1
    elif design[:len(towel)] == towel:
      remaining.append(design[len(towel):])
  
  result += sum([num_arrangements(x) for x in remaining])
  memo[design] = result
  return result

total = 0
for idx, design in enumerate(designs):
  print(f"design: {design} ({idx + 1}/{len(designs)})")
  arrangements = num_arrangements(design)
  print(arrangements)
  total += arrangements

print(total)
