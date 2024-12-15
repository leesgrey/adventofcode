import re

machines = []  # ((A, B), (x, y))
p2_add = 0
#p2_add = 10000000000000

with open('input.txt') as f:
    buttons = [None, None]
    for idx, line in enumerate(f):
        numbers = [int(x) for x in re.findall("[0-9]+", line)]
        match idx % 4:
            case 0:  # a
                buttons[0] = (numbers[0], numbers[1])
            case 1:  # b
                buttons[1] = (numbers[0], numbers[1])
            case 2:  # prize
                machines.append(((buttons[0], buttons[1]), (numbers[0] + p2_add, numbers[1] + p2_add)))
            case _:
                pass

def get_square(machine):
    (x_A, y_A), (x_B, y_B) = machine[0]

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

    return (x_A * n) + (x_B * m), (n * 3) + m

memo = {}
x_A = None
y_A = None
x_B = None
y_B = None

def get_num_coins_required(goal, cost, depth):
    global memo, x_A, y_A, x_B, y_B
    (x_P, y_P) = goal

    #if (depth > 200):
    #    return None

    if (x_P == 0) and (y_P == 0):
        return cost
    
    if (x_P < 0) or (y_P < 0):
        return None

    if (x_P, y_P) in memo:
        return memo[(x_P, y_P)]

    results = list(filter(lambda x: x is not None, [get_num_coins_required((x_P - x_A, y_P - y_A), cost + 3, depth + 1),
                                                    get_num_coins_required((x_P - x_B, y_P - y_B), cost + 1, depth + 1)]))
    if len(results) == 0:
        result = None
    else:
        result = min(results)
    memo[goal] = result
    return result

sum = 0
for machine in machines:
    #print(f"\n{machine}")
    cost = 0
    memo = {}
    (x_A, y_A), (x_B, y_B) = machine[0]

    size, square_cost = get_square(machine)
    #print(f"square: size {size}, cost {square_cost}")

    if size is not None:
        #fit_squares = min([machine[1][0] // size, machine[1][1] // size])
        fit_squares = min([p2_add // size, p2_add // size])
        cost += fit_squares * square_cost
    else:
        print(f"wuh: {machine}")
        fit_squares = 0
        size = 0
    remaining = (machine[1][0] - (fit_squares * size), machine[1][1] - (fit_squares * size))
    #print(f"{fit_squares} squares reach ({fit_squares * size}, {fit_squares * size}) before remaining {remaining}")

    num_coins_required = get_num_coins_required((remaining[0], remaining[1]), 0, 0)
    if num_coins_required is not None:
        #print(f"requires {num_coins_required} + {cost} coins")
        sum += num_coins_required + cost
    #else:
        #print("no")

print(f"\nsum: {sum}")