map = open('input.txt', 'r').read().strip().splitlines()

elf_locations = set()

for y, line in enumerate(map):
    map[y] = list(line)
    for x, char in enumerate(map[y]):
        if char == '#':
            elf_locations.add((x, y))

current_start = 0

directions = {'N': (0, -1), 'NE': (1, -1), 'NW': (-1, -1), 'S': (0, 1), 'SE': (1, 1), 'SW': (-1, 1), 'W': (-1, 0), 'E': (1, 0)}
direction_list = ('N', 'S', 'W', 'E')
print(elf_locations)

boo = 0
while boo < 10:
    new_elves = set()
    candidates = {}
    no_elves_around_counter = 0
    elf_locations_copy = {*elf_locations}
    while len(elf_locations) != 0:
        x, y = elf_locations.pop()
        elves_around = False
        for direction in directions.values():
            new_x = x + direction[0]
            new_y = y + direction[1]
            if (new_x, new_y) in elf_locations_copy:
                elves_around = True
                break
        if not elves_around:
            no_elves_around_counter += 1
            new_elves.add((x, y))
            continue
        found_proposed = False
        for i in range(current_start, current_start+4):
            if found_proposed:
                break
            real_i = i % 4
            elves_to_the_direction = False
            if direction_list[real_i] == 'N':
                for direction in {'N', 'NE', 'NW'}:
                    x_dir, y_dir = directions[direction]
                    new_x = x + x_dir
                    new_y = y + y_dir
                    if (new_x, new_y) in elf_locations_copy:
                        elves_to_the_direction = True
                        break
                if not elves_to_the_direction:
                    found_proposed = True
                    if (x, y-1) not in candidates.keys():
                        candidates[(x, y-1)] = (x, y)
                    else:
                        new_elves.add((x, y))
                        temp = candidates[(x, y-1)]
                        new_elves.add(temp)
                else:
                    continue
            elif direction_list[real_i] == 'S':
                for direction in {'S', 'SE', 'SW'}:
                    x_dir, y_dir = directions[direction]
                    new_x = x + x_dir
                    new_y = y + y_dir
                    if (new_x, new_y) in elf_locations_copy:
                        elves_to_the_direction = True
                        break
                if not elves_to_the_direction:
                    found_proposed = True
                    if (x, y+1) not in candidates.keys():
                        candidates[(x, y+1)] = (x, y)
                    else:
                        new_elves.add((x, y))
                        temp = candidates[(x, y+1)]
                        new_elves.add(temp)
                else:
                    continue
            elif direction_list[real_i] == 'W':
                for direction in {'W', 'SW', 'NW'}:
                    x_dir, y_dir = directions[direction]
                    new_x = x + x_dir
                    new_y = y + y_dir
                    if (new_x, new_y) in elf_locations_copy:
                        elves_to_the_direction = True
                        break
                if not elves_to_the_direction:
                    found_proposed = True
                    if (x-1, y) not in candidates.keys():
                        candidates[(x-1, y)] = (x, y)
                    else:
                        new_elves.add((x, y))
                        temp = candidates[(x-1, y)]
                        new_elves.add(temp)
                else:
                    continue
            elif direction_list[real_i] == 'E':
                for direction in {'E', 'SE', 'NE'}:
                    x_dir, y_dir = directions[direction]
                    new_x = x + x_dir
                    new_y = y + y_dir
                    if (new_x, new_y) in elf_locations_copy:
                        elves_to_the_direction = True
                        break
                if not elves_to_the_direction:
                    found_proposed = True
                    if (x+1, y) not in candidates.keys():
                        candidates[(x+1, y)] = (x, y)
                    else:
                        new_elves.add((x, y))
                        temp = candidates[(x+1, y)]
                        new_elves.add(temp)
                else:
                    continue
        if not found_proposed:
            new_elves.add((x, y))
    
    if no_elves_around_counter == len(elf_locations_copy):
        elf_locations = new_elves
        break

    for coords, og_coords in candidates.items():
        if og_coords in new_elves:
            continue

        new_elves.add(coords)
    elf_locations = new_elves
    # print(sorted(list(elf_locations), key=lambda x: x[1]))
    current_start = (current_start + 1) % 4
    # [(2, 0), (3, 0), (2, 2), (3, 3), (2, 4)]
    # [(2, 1), (3, 1), (1, 2), (4, 3), (2, 5)]
    # [(2, 0), (4, 1), (0, 2), (4, 3), (2, 5)]
    boo += 1
    
elves_list = list(elf_locations)
sorted_by_x = sorted(elves_list, key=lambda x: x[0])
lowest_x = sorted_by_x[0][0]
highest_x = sorted_by_x[-1][0]
sorted_by_y = sorted(elves_list, key=lambda x: x[1])
lowest_y = sorted_by_y[0][1]
highest_y = sorted_by_y[-1][1]

print(sorted(list(elf_locations), key=lambda x: x[1]))
print(abs(lowest_y - highest_y) + 1, abs(lowest_x - highest_x) + 1)


result = (abs(lowest_x - highest_x) + 1) * (abs(lowest_y - highest_y) + 1) - len(elf_locations)
print("Result: {}".format(result))
