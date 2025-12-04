banks = []

with open('input.txt') as f:
    for bank in f:
        banks.append([int(i) for i in bank[:-1]]) # newline

total = 0
for bank in banks:
    left = 0
    for i in range(12):
        # find largest
        largest_idx = left
        for idx in range(left, len(bank) - 11 + i):
            if bank[idx] > bank[largest_idx]:
                largest_idx = idx
        left = largest_idx + 1
        
        total += bank[largest_idx] * (10 ** (11 - i))

print(total)