reports = []

with open('input.txt') as f:
  for line in f:
    reports.append([int(x) for x in line.split()])

safe_count = 0

for report in reports:
  if len(report) < 2:
    continue

  last_diff = 0;
  safe = True

  for pair_idx in (range(len(report) - 1)):
    diff = report[pair_idx] - report[pair_idx + 1]
    if (diff == 0) or (last_diff * diff < 0) or (abs(diff) > 3):
      safe = False
      break
    last_diff = diff

  if safe:
    safe_count += 1
  
print(safe_count)