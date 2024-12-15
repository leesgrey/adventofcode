a = (94, 34)
b = (22, 67)

f = open("output.txt", "w")
f.write(f"a: {a}\n")
f.write(f"b: {b}\n")

def get_square(buttons):
    (x_A, y_A), (x_B, y_B) = buttons

    a, b = (y_B - x_B), (x_A - y_A)
    while b:
        a, b = b, a % b
    gcd = a
    if (gcd is None):
        return None, None

    n = (y_B - x_B) // gcd
    m = (x_A - y_A) // gcd
    print(f"n: {n}, m: {m}")
    f.write(f"n: {n}, m: {m}\n")

    if (n < 0) or (m < 0):
        return None, None

    return (x_A * n) + (x_B * m), (n * 3) + m

size, cost = get_square((a, b))
print(f"square: size {size}, cost {cost}")
f.write(f"square: size {size}, cost {cost}\n")

x_itr = 0
y_itr = 0

memo = {}
x_A = None
y_A = None
x_B = None
y_B = None

def get_num_coins_required(goal, cost, depth):
    global memo, x_A, y_A, x_B, y_B
    (x_P, y_P) = goal

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

for mult_square in range(3):
    f.write(f"\nsquares: {mult_square}")
    success = 0
    fail = 0
    for x_itr in range(size):
        for y_itr in range(size):
            target = ((mult_square * size) + x_itr, (mult_square * size) + y_itr) 
            machine = ((a, b), target)
            print(f"\n{machine}")
            memo = {}
            (x_A, y_A), (x_B, y_B) = machine[0]

            if size is None:
                #print("size none")
                fail += 1
                continue

            #fit_squares = min([machine[1][0] // size, machine[1][1] // size])
            #fit_squares = min([p2_add // size, p2_add // size])
            #remaining = (machine[1][0] - (fit_squares * size), machine[1][1] - (fit_squares * size))
            #print(f"{fit_squares} squares reach ({fit_squares * size}, {fit_squares * size}) before remaining {remaining}")

            num_coins_required = get_num_coins_required(target, 0, 0)
            num_coins_required = get_num_coins_required(remaining, 0, 0)
            if num_coins_required is not None:
                #print(f"requires {num_coins_required} + {cost} coins")
                f.write(f"\n{x_itr, y_itr}: {machine[1]}")
                success += 1
            else:
                #print("no")
                fail += 1
    f.write(f"\nsuccess: {success}, fail: {fail}\n")

f.close()