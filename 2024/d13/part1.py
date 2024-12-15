import re

machines = []  # ((A, B), (x, y))

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
                # create machine
                machines.append(((buttons[0], buttons[1]), (numbers[0], numbers[1])))
            case _:
                pass

#print(machines)

memo = {}
x_A = None
y_A = None
x_B = None
y_B = None
def get_num_coins_required(goal, cost):
    global memo, x_A, y_A, x_B, y_B
    (x_P, y_P) = goal

    if (x_P == 0) and (y_P == 0):
        return cost
    
    if (x_P < 0) or (y_P < 0):
        return None

    # add pruning for 100 condition

    if (x_P, y_P) in memo:
        return memo[(x_P, y_P)]

    results = list(filter(lambda x: x is not None, [get_num_coins_required((x_P - x_A, y_P - y_A), cost + 3),
                                                    get_num_coins_required((x_P - x_B, y_P - y_B), cost + 1)]))
    if len(results) == 0:
        result = None
    else:
        result = min(results)
    memo[goal] = result
    return result

sum = 0
for machine in machines:
    #print(f"\nmachine {machine}")
    (x_A, y_A), (x_B, y_B) = machine[0]
    memo = {}
    num_coins_required = get_num_coins_required(machine[1], 0)
    if num_coins_required is not None:
        #print(f"requires {num_coins_required} coins")
        sum += num_coins_required
    #else:
        #print("prize not winnable :(")

print(sum)