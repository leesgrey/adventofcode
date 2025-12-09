fresh_ranges = []
available_ids = set()

with open('input.txt') as f:
    reading_range = True
    for line in f:
        if line == "\n":
            reading_range = False
        elif reading_range:
            fresh_ranges.append([int(n) for n in line[:-1].split("-")])
        else:
            available_ids.add(int(line[:-1]))

fresh_ranges.sort(key = lambda x: x[0])

fresh_available = 0
for id in available_ids:
    if (next((fresh_range for fresh_range in fresh_ranges if (fresh_range[0] <= id and fresh_range[1] >= id)), None) != None):
        fresh_available += 1

print(fresh_available)
