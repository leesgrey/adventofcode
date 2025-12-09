fresh_ranges = []

with open('input.txt') as f:
    for line in f:
        if line == "\n":
            break
        else:
            fresh_ranges.append([int(n) for n in line[:-1].split("-")])

fresh_ranges.sort(key = lambda x: x[0])
condensed_ranges = [fresh_ranges[0]]

for fresh_range in fresh_ranges[1:]:
    if fresh_range[0] <= condensed_ranges[-1][1]:
        print("wah!")
        if fresh_range[1] > condensed_ranges[-1][1]:
            condensed_ranges[-1][1] = fresh_range[1]
    else:
        condensed_ranges.append(fresh_range)
    
total = 0
for condensed_range in condensed_ranges:
    total += condensed_range[1] - condensed_range[0] + 1
