import re
from tqdm import tqdm

#P2_ADD = 10000000000000
P2_ADD = 0

class Machine:
    def __init__(self, A, B, prize):
        self.A = A
        self.B = B
        self.prize = prize
    
    def __repr__(self):
        return f"Machine(A={self.A}, B={self.B}, self={self.prize})"

# file parsing
machines = []
with open('sample.txt') as f:
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

#print(machines)

memo = {}


def get_square(machine):
    (x_A, y_A), (x_B, y_B) = machine.A, machine.B

    a, b = (y_B - x_B), (x_A - y_A)
    while b:
        a, b = b, a % b
    gcd = a
    if (gcd is None):
        return None, None

    n = (y_B - x_B) // gcd
    m = (x_A - y_A) // gcd

    if (n < 0) or (m < 0):
        return None, None

    return (x_A * n) + (x_B * m), (n, m)


def get_presses_required(machine, goal, presses):
    if (goal == (0, 0)):
        return presses
    
    if (goal[0] < 0) or (goal[1] < 0):
        return None

    if goal in memo:
        #print(f"{goal} in memo")
        return memo[goal]

    results = list(filter(lambda x: x is not None, [get_presses_required(machine, (goal[0] - machine.A[0], goal[1] - machine.A[1]), (presses[0] + 1, presses[1])),
                                                    get_presses_required(machine, (goal[0] - machine.B[0], goal[1] - machine.B[1]), (presses[0], presses[1] + 1))]))

    if len(results) == 0:
        result = None
    else:
        result = min(results)
    memo[goal] = result
    return result


sum = 0
for machine in tqdm(machines):
    print(f"\n{machine}")
    print(get_square(machine))
    memo.clear()
    presses = get_presses_required(machine, machine.prize, (0, 0))
    if presses is not None:
        num_coins_required = (presses[0] * 3) + presses[1]
        print(f"requires {presses[0]} A presses and {presses[1]} B presses - {num_coins_required} coins")
        sum += num_coins_required
    else:
        print("prize not winnable :(")
        pass

print(sum)