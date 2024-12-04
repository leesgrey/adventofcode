import re

input = ""

with open('input.txt') as f:
  input = f.read()

print(input)

matches = re.findall("mul\([0-9]*\,[0-9]*\)|do\(\)|don't\(\)", input)

print(matches)

sum = 0
skip = False

for match in matches:
  instruction = re.search("mul\(|do\(|don\'t\(", match).group()
  if instruction[0] == "m":
    if skip:
      continue
    numbers = re.findall("[0-9]+", match)
    sum += int(numbers[0]) * int(numbers[1])
  elif instruction[2] == "n":
    skip = True
  else:
    skip = False

print(sum)
