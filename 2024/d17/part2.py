a = None
b = None
c = None

with open('input.txt') as f:
  a_line = f.readline()
  a = int(a_line.split()[-1])
  b_line = f.readline()
  b = int(b_line.split()[-1])
  c_line = f.readline()
  c = int(c_line.split()[-1])
  f.readline()
  program_line = f.readline()
  program = [int(x) for x in program_line.split()[1].split(',')]

print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}")
print(f"program: {program}")

instruction_pointer = 0
output = []

history = []

def combo(operand):
  assert operand != 7
  match operand:
    case 4:
      return a
    case 5:
      return b
    case 6:
      return c
    case _:
      return operand

while instruction_pointer < len(program):
  opcode = program[instruction_pointer]
  operand = program[instruction_pointer + 1]
  history.append((opcode, operand))

  match opcode:
    case 0:  # adv
      a = a // (2 ** combo(operand))
    case 1:  # bxl
      b = b ^ operand
    case 2:  # bst
      b = combo(operand) % 8
    case 3:  # jnz
      if a != 0:
        instruction_pointer = operand
        continue
    case 4:  # bxc
      b = b ^ c
    case 5:  # out
      output.append(combo(operand) % 8)
    case 6:  # bdv
      b = a // (2 ** combo(operand))
    case 7:
      c = a // (2 ** combo(operand))
  
  instruction_pointer += 2

print(",".join([str(x) for x in output]))

"""
Program: 2,4,1,1,7,5,4,6,0,3,1,4,5,5,3,0
(2 4)
(1 1)
(7 5)
(4 6)
(0 3)
(1 4)
(5 5)
(3 0)
"""
"""
print(program)
a0 = (8 ** (len(program) - 1))
idx = 0

a = 0
b = 0
c = 0
while True:
  b = (((a % 8) ^ 1) ^ (a // (2 ** ((a % 8) ^ 1)))) ^ 4
  c = a // (2 ** ((a % 8) ^ 1))
  a = a // 8

  if (b % 8) != program[idx]:
    # restart
    a0 += 1
    if (a0 > (8 ** (len(program)))):
      print("too a0 too big i think :()")
      break
    print(f"trying a0 = {a0}, idx = {idx}")
    a = a0
    b = 0
    c = 0
    idx = 0
    continue
  else:
    # matching
    idx += 1

  if (a == 0):
    if (idx == len(program)):
      print(f'yay - a0 = {a0}')
      break

    else:
      # restart
      a0 += 1
      if (a0 > (8 ** (len(program)))):
        print("too a0 too big i think :()")
        break
      print(f"trying a0 = {a0}, idx = {idx}")
      a = a0
      b = 0
      c = 0
      idx = 0
      continue
"""