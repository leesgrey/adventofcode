"""
Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
(0 1)
(5 4)
(3 0)
"""
program = [0, 1, 5, 4, 3, 0]

a = 0
b = 0
c = 0

a0 = 0
idx = 0

while True:
  a = a // (2 ** 3)

  # check value
  if (a % 8) != program[idx]:
    # reset
    a0 += 1
    print(f"trying a0 = {a0}")
    a = a0
    b = 0
    c = 0
    idx = 0
    continue
  else:
    idx += 1

  # check jump
  if (a == 0):
    if (idx != len(program)):
      # reset
      a0 += 1
      print(f"trying a0 = {a0}")
      a = a0
      b = 0
      c = 0
      idx = 0
      continue
    else:
      print(f"yay: {a0}")
      break