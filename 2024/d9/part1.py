diskmap = [] # [1, 2, 3, 4, 5]

with open('input.txt') as f:
  diskmap = [int(x) for x in list(f.read().strip())]

disk = []
last_file_idx = 0

is_file = True
spaces_before_file = 0
for idx, val in enumerate(diskmap):
  if is_file:
    disk.extend([idx // 2] * val)
    last_file_idx += (spaces_before_file + val)
    spaces_before_file = 0
  else:
    disk.extend([None] * val)
    spaces_before_file = val
  is_file = not is_file
last_file_idx -= 1

def get_checksum():
  global last_file_idx
  global disk
  checksum = 0
  for idx in range(len(disk)):
    if (idx > last_file_idx):
      return checksum

    if (disk[idx] is None):
      while disk[last_file_idx] is None:
        last_file_idx -= 1
      if (idx > last_file_idx):
        return checksum
      disk[idx] = disk[last_file_idx]
      disk[last_file_idx] = None
      last_file_idx -= 1
    
    checksum += (idx * disk[idx])
  
print(get_checksum())
