import re

#P2_ADD = 0
P2_ADD = 10000000000000

machines = []  # ((A, B), (x, y))

class Machine:
    def __init__(self, A, B, prize):
        self.A = A
        self.B = B
        self.prize = prize
    
    def __repr__(self):
        return f"Machine(A={self.A}, B={self.B}, self={self.prize})"

# file parsing
machines = []
with open('input.txt') as f:
    A = None
    B = None
    for idx, line in enumerate(f):
        numbers = [int(x) for x in re.findall("[0-9]+", line)]
        match idx % 4:
            case 0:  # a
                A = (numbers[0], numbers[1])
            case 1:  # b
                B = (numbers[0], numbers[1])
            case 2:  # prize
                # create machine
                machines.append(Machine(A, B, (numbers[0] + P2_ADD, numbers[1] + P2_ADD)))
            case _:
                pass

def get_coins(machine):
    m = ((machine.A[0] * machine.prize[1]) - (machine.A[1] * machine.prize[0])) / ((machine.A[0] * machine.B[1]) - (machine.A[1] * machine.B[0]))
    n = (machine.prize[0] - (machine.B[0] * m)) / machine.A[0]
    return (n, m)

total = 0
for machine in machines:
    print(machine)
    n, m = get_coins(machine)
    if (int(n) != n) or (int(m) != m):
        print('skip\n')
        continue
    print(f"a: {n}, b: {m}, cost: {(n * 3) + m}\n")
    total += (n * 3) + m

print(f"total: {total}")



