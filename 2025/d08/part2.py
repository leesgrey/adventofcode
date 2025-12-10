def get_dist_sq(a, b):
    return abs(((b[0] - a[0]) ** 2) + ((b[1] - a[1]) ** 2) + ((b[2] - a[2]) ** 2))

box_positions = []
with open('input.txt') as f:
    for line in f:
        box_positions.append(tuple(int(x) for x in line[:-1].split(',')))

pair_to_distance = {}
for box_a in box_positions:
    for box_b in box_positions:
        pair_tuple = (box_a, box_b)
        if (pair_tuple not in pair_to_distance) and ((box_b, box_a) not in pair_to_distance):
            distance = get_dist_sq(box_a, box_b)
            if (distance == 0):
                continue

            pair_to_distance[pair_tuple] = distance

distances = list(pair_to_distance.items())
distances.sort(key = lambda x: x[1])

circuits = []

for (box_a, box_b), distance in distances:
    a_circuit = None
    b_circuit = None
    for idx, circuit in enumerate(circuits):
        if box_a in circuit:
            circuit.add(box_b)
            a_circuit = idx
        elif box_b in circuit:
            circuit.add(box_a)
            b_circuit = idx 
    if ((a_circuit is not None) and (b_circuit is not None)):
        if (a_circuit < b_circuit):
            circuits[a_circuit] = circuits[a_circuit].union(circuits[b_circuit])
            del circuits[b_circuit]
        else:
            circuits[b_circuit] = circuits[b_circuit].union(circuits[a_circuit])
            del circuits[a_circuit]

    elif ((a_circuit is None) and (b_circuit is None)):
        circuits.append({box_a, box_b})
    
    if (len(circuits) == 1) and (len(circuits[0]) == len(box_positions)):
        print("box_a:", box_a)
        print("box_b:", box_b)
        print(box_a[0] * box_b[0])
        break
