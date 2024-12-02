
reports = []

with open('input.txt') as f:
  for line in f:
    reports.append([int(x) for x in line.split()])

safe_count = 0

def is_safe(report, recurse):
  safe = True
  last_diff = 0;

  for pair_idx in (range(len(report) - 1)):
    diff = report[pair_idx] - report[pair_idx + 1]
    if (diff == 0) or (last_diff * diff < 0) or (abs(diff) > 3):
      safe = False
      break
    last_diff = diff

  # base is_safe
  if ((not safe) and recurse):
    has_safe_removal = False
    for level_idx in range(len(report)):
      if is_safe(report[:level_idx] + report[level_idx + 1:], False):
        has_safe_removal = True
        break
    return has_safe_removal
  else:
    return safe

for report in reports:
  safe = is_safe(report, True)

  if safe:
    safe_count += 1

print(safe_count)