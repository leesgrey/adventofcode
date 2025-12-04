banks = []

with open('input.txt') as f:
    for bank in f:
        banks.append([int(i) for i in bank[:-1]]) # newline

total = 0
for bank in banks:
    # find largest tens
    tens_idx = 0
    for idx in range(1, len(bank) - 1):
        if bank[idx] > bank[tens_idx]:
            tens_idx = idx
    
    # find largest one after
    ones_idx = tens_idx + 1
    for idx in range(ones_idx + 1, len(bank)):
        if bank[idx] > bank[ones_idx]:
            ones_idx = idx
    
    total += (bank[tens_idx] * 10) + bank[ones_idx]

print(total)