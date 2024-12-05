import re

rules = []
updates = []

with open('input.txt') as f:
  newline_seen = False

  for line in f:
    if newline_seen:
      updates.append([int(x) for x in re.findall('[0-9]+', line[:-1])])
      continue

    elif line == "\n":
      newline_seen = True
    else:
      rules.append([int(x) for x in re.findall('[0-9]+', line[:-1])])

rules_map = {}
for rule in rules:
  if rule[0] not in rules_map:
    rules_map[rule[0]] = [rule[1]]
  else:
    rules_map[rule[0]].append(rule[1])

def check_update_correctness(update):
  page_to_index = {}
  for idx, page in enumerate(update):
    page_to_index[page] = idx

  for page in update:
    if page not in rules_map:
      continue
    pages_to_be_before = rules_map[page]
    for page_to_be_before in pages_to_be_before:
      if (page_to_be_before in page_to_index) and (page_to_index[page_to_be_before] < page_to_index[page]):
        return False
  
  return True

def add_page_to_corrected_update(page, corrected_update):
  if page not in rules_map:
    return corrected_update + [page]

  pages_to_be_before = rules_map[page]
  for idx, previous_page in enumerate(corrected_update):
    if previous_page in pages_to_be_before:
      return corrected_update[:idx] + [page] + corrected_update[idx:]
  return corrected_update + [page]

def correct_update(update):
  correct = []
  correct.append(update[0])
  for page in update[1:]:
    correct = add_page_to_corrected_update(page, correct)
  return correct

sum = 0
for update in updates:
  if check_update_correctness(update):
    continue
  corrected_update = correct_update(update)
  sum += corrected_update[len(corrected_update) // 2]

print(sum)