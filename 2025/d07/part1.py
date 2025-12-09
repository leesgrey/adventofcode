beams = set()
num_splits = 0

with open('input.txt') as f:
    first_line = f.readline()
    beams.add(first_line.index("S"))

    for line in f:
        for idx, c in enumerate(line):
            if c == "^" and idx in beams:
                beams.remove(idx)
                if idx - 1 >= 0:
                    beams.add(idx - 1)
                if idx + 1 < len(line):
                    beams.add(idx + 1)
                num_splits += 1
                
print(num_splits)