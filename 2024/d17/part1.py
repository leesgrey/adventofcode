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

print(output)
print(",".join([str(x) for x in output]))