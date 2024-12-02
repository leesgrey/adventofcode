l1 = []
l2 = []

with open('input.txt') as f:
  for line in f:
    a, b = line.split()
    l1.append(int(a))
    l2.append(int(b))

l1.sort()
l2.sort()

total_distance = 0
for idx, pair in enumerate(l1):
  total_distance += abs(l1[idx] - l2[idx])

print(total_distance)
