import re

input = ""

with open('input.txt') as f:
  input = f.read()

print(input)

mul_matches = re.findall("mul\([0-9]*\,[0-9]*\)", input)

print(mul_matches)

sum = 0

for match in mul_matches:
  numbers = re.findall("[0-9]+", match)
  print(numbers)
  sum += int(numbers[0]) * int(numbers[1])

print(sum)
