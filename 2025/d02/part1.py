ranges = []

with open('input.txt') as f:
    ranges_line = f.readline()
    ranges = [str_range.split('-') for str_range in ranges_line.split(',')]

sum = 0
for range in ranges:
    start = range[0]
    length = len(start)
    half = int(start[:(length//2)]) if length > 1 else 0
    candidate = (half * (10 ** (length //2))) + half

    while (candidate <= int(range[1])):
        if (candidate >= int(start)):
            sum += candidate
        half += 1
        candidate = (half * (10 ** (length //2))) + half

print(sum)