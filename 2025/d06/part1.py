import math

problem_inputs = []
operators = []

with open('input.txt') as f:
    firstline = f.readline()
    problem_inputs = [[int(n)] for n in firstline.split()]
    for line in f:
        if line[0] == "+" or line[0] == "*":
            operators = line.split()
        else:
            for idx, num in enumerate(line.split()):
                problem_inputs[idx].append(int(num))

total = 0
for problem in zip(problem_inputs, operators):
    if problem[1] == "*":
        total += math.prod(problem[0])
    else:
        total += sum(problem[0])

print(total)