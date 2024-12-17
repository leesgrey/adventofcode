grid = []

with open('input.txt') as f:
    for row in f:
        grid.append(list(row.strip()))

def plant_at(coords):
    global grid
    if (coords[0] < 0) or (coords[1] < 0) or (coords[0] >= len(grid)) or (coords[1] >= len(grid[0])):
        return None
    return grid[coords[0]][coords[1]]

def get_neighbors(coords):
    return [(coords[0] - 1, coords[1]),
            (coords[0], coords[1] + 1),
            (coords[0] + 1, coords[1]),
            (coords[0], coords[1] - 1)]

regions = {}  # {plant: [({(coords), ...}, {(dir): [(coords), ...], ...}), ...]}

plots_in_region = set()  # [(coords), ...]
for row_idx, row in enumerate(grid):
    for col_idx, plant in enumerate(row):
        current_plot = (row_idx, col_idx)
        if current_plot in plots_in_region:
            #print(f"{current_plot} already in {plant} region")
            continue

        # create region
        if plant not in regions:
            regions[plant] = []
        #print(f"\ncreating new {plant} region from {current_plot}")
        regions[plant].append((set(), {}))
        plots = regions[plant][-1][0]
        edges = regions[plant][-1][1]  # {(direction): [(coords), ...], ...}
        plots_in_current_region = set()

        # expand region through neighbors
        plots_with_origin = [(current_plot, current_plot)]
        while len(plots_with_origin) != 0:
            checking, origin = plots_with_origin.pop()
            if checking in plots:
                continue

            if plant_at(checking) != plant:
                direction = (checking[0] - origin[0], checking[1] - origin[1])
                if direction in edges:
                    edges[direction].add(origin)
                else:
                    edges[direction] = {origin}
            else:
                plots.add(checking)
                plots_with_origin.extend([(x, checking) for x in get_neighbors(checking)])
                plots_in_region.add(checking)
                plots_in_current_region.add(checking)
        #print(f"plots: {plots}")
        #print(f"edges: {edges}")

total_price = 0
for plant in regions:
    for region in regions[plant]:
        total_edges = 0
        for direction in region[1]:
            layers = {}
            if direction[0] == 0:  # vertical edge
                idx_of_layer = 1
                length = len(grid)
            else:
                idx_of_layer = 0  # horizontal edge
                length = len(grid[0])
            
            #print(f"\n{idx_of_layer} {plant} edges: {region[1][direction]}")
            for edge in region[1][direction]:
                layer = edge[idx_of_layer]
                if layer in layers:
                    layers[layer].add(edge[1 - abs(idx_of_layer)])  # the other one
                else:
                    layers[layer] = {edge[1 - abs(idx_of_layer)]}
            
            edges = 0
            for layer in layers:
                edge_started = False
                for scan_idx in range(length):
                    if scan_idx in layers[layer]:
                        edge_started = True
                    elif edge_started:
                        edges += 1
                        edge_started = False
                if edge_started:
                    edges += 1
            total_edges += edges
        #print(f"\n{plant} region had {total_edges} edges and a price of {len(region[0])} * {total_edges} = {total_edges * len(region[0])}")
        total_price += (total_edges * len(region[0]))

print(total_price)