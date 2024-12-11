stones = []

with open('input.txt') as f:
  stones = [int(x) for x in list(f.read().split())]

stones_count = {}

for stone in stones:
  if stone in stones_count:
    stones_count[stone] += 1
  else:
    stones_count[stone] = 1

def add_stones(stone, num):
  global stones_count
  if stone in stones_count:
    stones_count[stone] += num
  else:
    stones_count[stone] = num

def remove_stones(stone, num):
  global stones_count
  stones_count[stone] -= num
  if stones_count[stone] == 0:
    del stones_count[stone]

memo = {}
blinks = 75
while blinks > 0:
  current_stones = stones_count.copy()
  for stone in current_stones:
    num = current_stones[stone]
    remove_stones(stone, num)
    if stone in memo:
      pass
    else:
      if stone == 0:
        add_stones(1, num)
        continue
      num_digits = len(str(stone))
      if num_digits % 2 == 0:
        add_stones(int(str(stone)[:(num_digits // 2)]), num)
        add_stones(int(str(stone)[(num_digits // 2):]), num)
      else:
        add_stones(stone * 2024, num)
  blinks -= 1

sum = 0
for stone in stones_count:
  sum += stones_count[stone]
print(sum)