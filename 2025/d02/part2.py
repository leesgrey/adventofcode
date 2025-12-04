ranges = []

with open('input.txt') as f:
    ranges_line = f.readline()
    ranges = [str_range.split('-') for str_range in ranges_line.split(',')]

total = 0
for search_range in ranges:
    start = search_range[0]
    end = search_range[1]
    added = set()

    for candidate_len in range(len(start), len(end) + 1):
        for seq_len in range(1, (candidate_len // 2) + 1):
            seq = 1 * (10 ** (seq_len - 1))
            candidate = str(seq) * (candidate_len // len(str(seq)))
            while (int(candidate) <= int(end) and (len(str(seq)) <= seq_len)):
                if (int(candidate) >= int(start)):
                    added.add(int(candidate))
                seq = seq + 1
                candidate = str(seq) * (candidate_len // len(str(seq)))
    total += sum(added)

print(total)