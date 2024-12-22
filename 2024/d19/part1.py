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
for towel in towels:
  memo[towel] = True

def match(design):
  #print(f"design: {design}")
  if design in memo:
    return memo[design]
  
  remaining = []
  for towel in towels:
    if design[:len(towel)] == towel:
      remaining.append(design[len(towel):])
  
  result = any([match(x) for x in remaining])
  memo[design] = result
  return result

sum = 0
for idx, design in enumerate(designs):
  print(f"design: {design} ({idx + 1}/{len(designs)})")
  if match(design):
    sum += 1

print(sum)
