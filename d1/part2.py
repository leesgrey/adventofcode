l1 = []
l2 = []

with open('input.txt') as f:
  for line in f:
    a, b = line.split()
    l1.append(int(a))
    l2.append(int(b))

counts = {}

for y in l2:
  if y in counts:
    counts[y] += 1
  else:
    counts[y] = 1

print(counts)
result = 0

for x in l1:
  if x in counts:
    result += (x * counts[x])
  
print(result)
