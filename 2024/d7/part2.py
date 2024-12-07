import re

equations = []

with open('input.txt') as f:
  for line in f:
    equations.append([int(x) for x in re.findall('[0-9]+', line)])

def is_solvable(current, target, remaining_values):
  if len(remaining_values) == 0:
    return current == target

  if current > target:
    return False

  return is_solvable(current * remaining_values[0], target, remaining_values[1:]) or is_solvable(current + remaining_values[0], target, remaining_values[1:]) or is_solvable(int(str(current) + str(remaining_values[0])), target, remaining_values[1:])

sum = 0
for equation in equations:
  target = equation[0]
  values = equation[1:]

  if is_solvable(values[0], target, values[1:]):
    sum += target

print(sum)