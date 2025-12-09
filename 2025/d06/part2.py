import math

operators = []
problem_widths = []

stripped_problem_inputs = []
with open('input.txt') as f:
    firstline = f.readline()
    problem_inputs = [[n] for n in firstline.split()]
    for line in f:
        if line[0] == "+" or line[0] == "*":
            operators = line.split()
        else:
            for idx, num in enumerate(line.split()):
                problem_inputs[idx].append(num)

problem_widths = []

for problem in problem_inputs:
    problem_widths.append(max([len(i) for i in problem]))

num_problems = len(operators)

parsed_problems = []
for problem_width in problem_widths:
    parsed_problems.append([''] * problem_width)

with open('input.txt') as f:
    for line in f:
        if line[0] == "+" or line[0] == "*":
            break

        problem_start_idx = 0
        for problem_idx in range(num_problems):
            for input_idx in range(problem_widths[problem_idx]):
                if line[problem_start_idx + input_idx] != " ":
                    parsed_problems[problem_idx][input_idx] += line[problem_start_idx + input_idx]

            problem_start_idx += problem_widths[problem_idx] + 1
        

total = 0
for problem in zip(parsed_problems, operators):
    if problem[1] == "*":
        total += math.prod([int(s) for s in problem[0]])
    else:
        total += sum([int(s) for s in problem[0]])

print(total)