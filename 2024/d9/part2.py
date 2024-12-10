diskmap = []

with open('input.txt') as f:
  diskmap = [int(x) for x in list(f.read().strip())]

disk = ""

files = []  # (idx, len)
spaces = []  # (idx, len)
is_file = True
cur_idx = 0
for idx, val in enumerate(diskmap):
  if is_file:
    files.append((cur_idx, val))
  else:
    spaces.append((cur_idx, val))
  cur_idx += val
  is_file = not is_file

checksum = 0
for file_id in range(len(files) - 1, -1, -1):
  file_length = files[file_id][1]
  for space_idx in range(len(spaces)):
    space_length = spaces[space_idx][1]
    if files[file_id][0] < spaces[space_idx][0]:
      break

    if file_length <= space_length:
      files[file_id] = (spaces[space_idx][0], files[file_id][1])
      spaces[space_idx] = (spaces[space_idx][0] + file_length, space_length - file_length)
      break

  for idk in range(file_length):
    checksum += file_id * (files[file_id][0] + idk)

print(checksum)