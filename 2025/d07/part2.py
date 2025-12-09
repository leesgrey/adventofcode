from collections import defaultdict

beam_to_timelines = defaultdict(int)

with open('input.txt') as f:
    first_line = f.readline()
    beam_to_timelines[first_line.index("S")] = 1

    i = 0
    for line in f:
        for idx, c in enumerate(line):
            if c == "^" and idx in beam_to_timelines:
                if idx - 1 >= 0:
                    beam_to_timelines[idx - 1] += beam_to_timelines[idx]
                if idx + 1 < len(line):
                    beam_to_timelines[idx + 1] += beam_to_timelines[idx]
                del beam_to_timelines[idx]
        i += 1

total = 0
for beam in beam_to_timelines:
    total += beam_to_timelines[beam]