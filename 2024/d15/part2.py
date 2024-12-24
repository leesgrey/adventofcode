from tqdm import tqdm

move_to_direction = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}

walls = set()
instructions = []
start = None
box_grid = []


class Box:
    def __init__(self):
        self.left = None
        self.right = None

    @staticmethod
    def pair_boxes(left, right):
        left.right = right
        right.left = left


reading_instructions = False
with open("input.txt") as f:
    for row, line in enumerate(f):
        stripped_line = line.strip()
        if len(stripped_line) == 0:
            reading_instructions = True
            continue
        if reading_instructions:
            instructions.extend(list(stripped_line))
        else:
            box_grid.append([None] * (len(stripped_line) * 2))
            for col, val in enumerate(list(stripped_line)):
                if val == "#":
                    walls.add((row, (col * 2)))
                    walls.add((row, (col * 2) + 1))
                elif val == "O":
                    box_grid[row][col * 2] = Box()
                    box_grid[row][(col * 2) + 1] = Box()
                    Box.pair_boxes(box_grid[row][col * 2], box_grid[row][(col * 2) + 1])
                elif val == "@":
                    start = (row, col * 2)


def print_state():
    for row in range(len(box_grid)):
        row_string = ""
        for col in range(len(box_grid[0])):
            if (row, col) in walls:
                row_string += "#"
            elif box_grid[row][col] is not None:
                row_string += "|"
            elif (row, col) == robot:
                row_string += "@"
            else:
                row_string += "."
        print(row_string)


def movable_boxes_in_direction(position, direction):
    box = box_grid[position[0]][position[1]]
    look_aheads = [(position[0] + direction[0], position[1] + direction[1])]
    other = None

    if box.left is not None:
        other = position[0], position[1] - 1
    else:
        other = position[0], position[1] + 1
    
    if (direction[1] == 0):  # horizontal
        look_aheads.append((other[0] + direction[0], other[1] + direction[1]))

    to_pass = set()
    for look_ahead in look_aheads:
        if look_ahead in walls:
            return []

        if (box_grid[look_ahead[0]][look_ahead[1]] is not None):
            next_movable = movable_boxes_in_direction(look_ahead, direction)
            if len(next_movable) > 0:
                to_pass.update(next_movable)
            else:
                return []

        to_pass.add(position)
        to_pass.add(other)
    
    sorted_pass = None
    match direction:
        case (0, -1):  # left
            sorted_pass = sorted(to_pass, key=lambda x: x[1])
        case (-1, 0):  # up
            sorted_pass = sorted(to_pass, key=lambda x: x[0])
        case (0, 1):  # right
            sorted_pass = sorted(to_pass, key=lambda x: x[1], reverse=True)
        case (1, 0):  # down
            sorted_pass = sorted(to_pass, key=lambda x: x[0], reverse=True)
            
    return sorted_pass


robot = start


for move in tqdm(instructions):
    #print(f"move: {move}")
    direction = move_to_direction[move]
    target = (robot[0] + direction[0], robot[1] + direction[1])

    if target in walls:
        #print("bonk wall")
        pass
    elif box_grid[target[0]][target[1]] is not None:
        movable = movable_boxes_in_direction(target, direction)
        #print(movable)
        if len(movable) > 0:
            for box_position in movable:
                box_grid[box_position[0] + direction[0]][
                    box_position[1] + direction[1]
                ] = box_grid[box_position[0]][box_position[1]]
                box_grid[box_position[0]][box_position[1]] = None
            robot = target
    else:
        robot = target
    #print_state()

total = 0
for row_idx, row in enumerate(box_grid):
    for col_idx, box in enumerate(row):
        if (box is not None) and (box.right is not None):
            total += (100 * row_idx) + col_idx

print(total)