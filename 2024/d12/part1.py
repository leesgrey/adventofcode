grid = []

with open('input.txt') as f:
    for row in f:
        grid.append(list(row.strip()))

def plant_at(coords):
    global grid
    if (coords[0] < 0) or (coords[1] < 0) or (coords[0] >= len(grid)) or (coords[1] >= len(grid[0])):
        return None
    return grid[coords[0]][coords[1]]

perimeters = {}
regions = {}
in_region = set()
num_regions = 0
for row_idx, row in enumerate(grid):
    for col_idx, plant in enumerate(row):
        if plant not in regions:
            regions[plant] = []

        coords = (row_idx, col_idx)
        # get perimeters
        perimeter = 0
        sides = [(row_idx - 1, col_idx),
                 (row_idx, col_idx + 1),
                 (row_idx + 1, col_idx),
                 (row_idx, col_idx - 1)]
        for side in sides:
            if plant_at(side) != plant:
                perimeter += 1
        perimeters[coords] = perimeter

        if coords in in_region:
            #print(f"{coords} already in {plant} region")
            continue
        
        #print(f"creating new {plant} region from {coords}")
        regions[plant].append({coords})
        in_region.add(coords)

        plots_to_check = sides.copy()
        while len(plots_to_check) != 0:
            current_plot = plots_to_check.pop()
            if current_plot in in_region:
                continue
            if plant_at(current_plot) == plant:
                regions[plant][-1].add(current_plot)
                plots_to_check.extend([(current_plot[0]- 1, current_plot[1]),
                                       (current_plot[0], current_plot[1] + 1),
                                       (current_plot[0] + 1, current_plot[1]),
                                       (current_plot[0], current_plot[1]- 1)])
                in_region.add(current_plot)
        #print(regions[plant][-1])

total_price = 0
for plant in regions:
    for region in regions[plant]:
        #print(f"{plant} region {len(region)} * {sum([perimeters[x] for x in region])}")
        total_price += len(region) * sum([perimeters[x] for x in region])

print(total_price)