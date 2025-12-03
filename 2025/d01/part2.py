rotations = []

with open('input.txt') as f:
    for line in f:
        if line[0] == "L":
            rotations.append(int(line[1:]) * -1)
        else:
            rotations.append(int(line[1:]))

def rotate(current: int, rotation: int):
    zeros = abs(rotation) // 100
    return ((current + rotation) % 100, zeros)

current = 50
password = 0

for rotation in rotations:
    new, zeros = rotate(current, rotation)
    if (new == 0):
        password += 1
    elif ((rotation < 0 and new > current and current != 0) or (rotation > 0 and new < current)):  # ew
        password += 1
    password += zeros
    current = new

print(password)