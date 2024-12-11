stones = []

with open('input.txt') as f:
  stones = [int(x) for x in list(f.read().split())]

stones_count = {}

for stone in stones:
  if stone in stones_count:
    stones_count[stone] += 1
  else:
    stones_count[stone] = 1

def increment_stone_count(stone, num):
  global stones_count
  if stone in stones_count:
    stones_count[stone] += num
  else:
    stones_count[stone] = num

memo = {}
blinks = 75
while blinks > 0:
  current_stones = stones_count.copy()
  for stone in current_stones:
    stones_count[stone] -= current_stones[stone]
    if stones_count[stone] == 0:
      del stones_count[stone]
    if stone in memo:
      pass
    else:
      if stone == 0:
        increment_stone_count(1, current_stones[stone])
        continue
      num_digits = len(str(stone))
      if num_digits % 2 == 0:
        increment_stone_count(int(str(stone)[:(num_digits // 2)]), current_stones[stone])
        increment_stone_count(int(str(stone)[(num_digits // 2):]), current_stones[stone])
      else:
        increment_stone_count(stone * 2024, current_stones[stone])
  blinks -= 1

sum = 0
for stone in stones_count:
  sum += stones_count[stone]
print(sum)