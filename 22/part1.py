from pprint import pprint
input = open('sample.txt', 'r').read().strip().splitlines()


instructions = []
for line in input:
    split_line = line.split(' ')
    split_coords = split_line[1].split(',')
    for i, split_cord in enumerate(split_coords):
        split_cord = split_cord.split('=')[1]
        split_coords[i] = split_cord.split('..')
        split_coords[i][0] = int(split_coords[i][0])
        split_coords[i][1] = int(split_coords[i][1])
    instructions.append([split_line[0]] + split_coords)
print(instructions)


# [(1, (x), (y), (z)), ()]
# lower_bounds = {1: [], 2: [], 3: []}
# upper_bounds = {1: [], 2: [], 3: []}

# def intersects(instruction, altered_instructions):
#     for altered in altered_instructions:
#         print(altered)
#         full_coverage = 0
#         partial_coverage = 0
#         for i in range(1, 4):
#             if altered[i][0] < instruction[i][0] and altered[i][1] > instruction[i][1]:
#                 full_coverage += 1
#             elif altered[i][0] < instruction[i][0] or altered[i][1] > instruction[i][1]:

#                 partial_coverage += 1
#         if full_coverage == 3:
#             print("ITS DINNER TIME")
#         print("FULL", full_coverage)
#         print("PARTIAL", partial_coverage)


on_cuboids = set()
altered_instructions = []
counter = 0
for instruction in instructions:
    print(counter)
    counter += 1
    continue_flag = False
    # for i in range(1, 4):
    # if instruction[i][0] < -50 or instruction[i][1] > 50:
    #     continue_flag = True
    #     break
    # if continue_flag:
    #     continue
    if instruction[0] == 'on':
        # if len(altered_instructions) != 0 and intersects(instruction, altered_instructions):
        #     print("YES")
        # altered_instructions.append(instruction)
        all_cubes = []
        for x in range(instruction[1][0], instruction[1][1]+1):
            for y in range(instruction[2][0], instruction[2][1]+1):
                for z in range(instruction[3][0], instruction[3][1]+1):
                    on_cuboids.add((x, y, z))
                    all_cubes.append((x, y, z))
    else:
        for x in range(instruction[1][0], instruction[1][1]+1):
            for y in range(instruction[2][0], instruction[2][1]+1):
                for z in range(instruction[3][0], instruction[3][1]+1):
                    if (x, y, z) in on_cuboids:
                        on_cuboids.remove((x, y, z))


# (10,12) x 3 power 27
# (11,13) x 3 power 27
# intersection (11, 12) x 3 power 8
# (10,12) x 3 power 27 - 8 = 19
# (11,13) x 3 power 27 - 8 = 19
# overall power 46
# (9,11) x 3
# intersections of (10, 12) x 3 = (11, 12) x 3
# intersection (11, 11) x 3
# -1
# intersection with


print(len(on_cuboids))

result = 0
print("Result: {}".format(result))
