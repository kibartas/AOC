from copy import deepcopy
from collections import Counter
input = open('input.txt', 'r').read().strip().splitlines()

instructions = []
for line in input:
    split_line = line.split(' ')
    split_coords = split_line[1].split(',')
    for i, split_cord in enumerate(split_coords):
        split_cord = split_cord.split('=')[1]
        split_coords[i] = split_cord.split('..')
        split_coords[i][0] = int(split_coords[i][0])
        split_coords[i][1] = int(split_coords[i][1])
        split_coords[i] = tuple(split_coords[i])
    split_coords = tuple(split_coords)
    instructions.append((split_line[0], split_coords))
# print(instructions)


# [(1, (x), (y), (z)), ()]
# lower_bounds = {1: [], 2: [], 3: []}
# upper_bounds = {1: [], 2: [], 3: []}

# def separating_axis(altered_instructions):
#     if


def find_intersection(x, y, intersections_x=[], intersections_y=[]):
    prod = 1
    # print(intersections_x, intersections_y)
    # print(x, y)
    # print(x, y)
    new_intersections = []
    for i in range(0, 3):
        if x[i][0] > y[i][1] or y[i][0] > x[i][1]:
            return 0, []
        bounds = None
        # f.e. (20, 30) (15, 30)
        if (x[i][0] >= y[i][0] and x[i][0] <= y[i][1]):
            bounds = (x[i][0], min(y[i][1], x[i][1]))
        # f.e. (20, 40) (30, 30)
        elif (x[i][1] >= y[i][0] and x[i][1] <= y[i][1]):
            bounds = (max(x[i][0], y[i][0]), x[i][1])
        elif (y[i][0] >= x[i][0] and y[i][0] <= x[i][1]):
            bounds = (y[i][0], min(y[i][1], x[i][1]))
        elif (y[i][1] >= x[i][0] and y[i][1] <= x[i][1]):
            bounds = (max(x[i][0], y[i][0]), y[i][1])
        prod *= abs(bounds[1] - bounds[0]) + 1
        # print(
        #     f"intersection from {bounds[0]} to {bounds[1]}", prod)
        new_intersections.append(bounds)
    return prod, tuple(new_intersections)


def every_point(instruction):
    every_p = []
    for x in range(instruction[0][0], instruction[0][1]+1):
        for y in range(instruction[1][0], instruction[1][1]+1):
            for z in range(instruction[2][0], instruction[2][1]+1):
                every_p.append((x, y, z))
    return every_p


on_cuboids_count = 0
blocks = []


def sign(x):
    return 1 if x >= 0 else -1


for i, ins in enumerate(instructions):
    print(i)
    blocks_copy = deepcopy(blocks)
    if ins[0] == 'on':
        if i != 0:
            for block in blocks_copy:
                overlap, new_intersection = find_intersection(ins[1], block[0])
                if len(new_intersection) != 0:
                    blocks.append(
                        [new_intersection, overlap * sign(block[1]) * -1])
        blocks.append([ins[1], find_intersection(ins[1], ins[1])[0]])
    elif ins[0] == 'off':
        for block in blocks_copy:
            overlap, new_intersection = find_intersection(ins[1], block[0])
            if len(new_intersection) != 0:
                blocks.append(
                    [new_intersection, overlap * sign(block[1]) * -1])

for block in blocks:
    print(block)
    on_cuboids_count += block[1]
# 14
# 9 + 9 - 4 = 15

# 15
# 9 + 9 + 4 - 4 - 2 - 2 + 1 =
# 9 + 9 - 2 - 2 + 1 =

# 20
# 9 + 9 + 9 + 4 = 31
# 31 - 4 - 4 - 2 - 1 = 20

# 26
# 9 + 9 + 9 + 16 + 4 = 47
# 47 - 4 - 4 - 2 - 1 - 4 - 6 - 3 - 4 =

# on x=-1..0,y=-1..1,z=-1..1
# on x=-1..0,y=-1..1,z=-0..0
# on x=-1..1,y=-0..0,z=-1..0
# on x=-1..0,y=-1..1,z=-1..1

# overall area (-1, 1) (-1, 1) (-1, 1) = 27 dark

# (10, 12) (10, 12) = big_cube
# (11, 13) (11, 13) big_cube = (10, 13) (10, 13)
# area in big cube 16
# 64 -


result = on_cuboids_count
print("Result: {}".format(result))

# [[10, 12], [10, 12], [10, 12]] [[10, 12], [10, 12], [10, 12]]
x = [[10, 12], [10, 12], [10, 12]]
y = [[9, 14], [11, 13], [11, 13]]
