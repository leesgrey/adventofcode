rotations = []

with open('input.txt') as f:
    for line in f:
        if line[0] == "L":
            rotations.append(int(line[1:]) * -1)
        else:
            rotations.append(int(line[1:]))

def rotate(current: int, rotation: int) -> int:
    return (current + rotation) % 100

current = 50
password = 0

for rotation in rotations:
    current = rotate(current, rotation)
    if (current == 0):
        password += 1

print(password)