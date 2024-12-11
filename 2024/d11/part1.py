stones = []

with open('input.txt') as f:
  stones = [int(x) for x in list(f.read().split())]

def blink(stones):
  for idx, stone in enumerate(stones):
    if type(stone) is list:
      blink(stone)
    elif stone == 0:
      stones[idx] = 1
      continue
    num_digits = len(str(stone))
    if num_digits % 2 == 0:
      stones[idx] = [int(str(stone)[:(num_digits // 2)]), int(str(stone)[(num_digits // 2):])]
    else:
      stones[idx] = stone * 2024

  return stones

count = 75
while count > 0:
  stones = blink(stones)
  count -= 1

def get_num_stones(stones):
  sum = 0
  for stone in stones:
    if type(stone) is list:
      sum += get_num_stones(stone)
    else:
      sum += 1
  return sum

print(get_num_stones(stones))