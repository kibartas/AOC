map, instructions = open('input.txt', 'r').read().split('\n\n')
instructions_list = []
number = ''
for char in instructions:
    if char.isnumeric():
        number += char
    else:
        if number != '':
            instructions_list.append(int(number))
            number = ''
        if char != '\n':
            instructions_list.append(char)
if number != '':
    instructions_list.append(int(number))

print(instructions_list)


map_file = open('maps.txt', 'w')

def write_map(map, current_pos, direction):
    for y, line in enumerate(map):
        for x, char in enumerate(line):
            if (x, y) == current_pos:
                if direction == 'R':
                    map_file.write('>')
                elif direction == 'L':
                    map_file.write('<')
                elif direction == 'D':
                    map_file.write('v')
                elif direction == 'U':
                    map_file.write('^')
            else:
                map_file.write(char)
        map_file.write('\n')
    map_file.write('\n\n')


def print_map(map, current_pos=None, direction=None):
    for y, line in enumerate(map):
        for x, char in enumerate(line):
            if (x, y) == current_pos:
                if direction == 'R':
                    print('>', end='')
                elif direction == 'L':
                    print('<', end='')
                elif direction == 'D':
                    print('v', end='')
                elif direction == 'U':
                    print('^', end='')
            else:
                print(char, end='')
        print()
    print('\n\n')

x_boundaries = {}

map = map.split('\n')
print(map)
map_width = max([len(line) for line in map])

for i in range(200):
    if i < 50:
        start = (0, 149-i, 'R')
        end = (99, 149-i, 'L')
    elif i < 100:
        start = (i-50, 100, 'D')
        end = (100+i-50, 49, 'U')
    elif i < 150:
        start = (50, 49-(i-100), 'R')
        end = (149, 49-(i-100), 'L')
    elif i < 200:
        start = (i-150+50, 0, 'D')
        end = (i-150+50,149, 'U')
    x_boundaries[i] = (start, end)
    map[i] = list(map[i])
    if len(map[i]) < map_width:
        map[i] += list(' ' * (map_width-len(map[i])))
    print(i, map[i])


y_boundaries = {}
for x in range(150):
    if x < 50:
        start = (50, 50+x, 'R')
        end = (100+x, 0, 'D')
    elif x < 100:
        start = (0, 150+x-50, 'R')
        end = (49, 150+x-50, 'L')
    elif x < 150:
        start = (x-100, 199, 'U')
        end = (99, 50+x-100, 'L')
    y_boundaries[x] = (start, end)

current_pos = (map[0].index('.'), 0)
direction = 'R'
# print_map(map, current_pos, direction)

for instruction in instructions_list:
    if isinstance(instruction, int):
        x, y = current_pos
        instruction_counter = instruction
        while instruction_counter != 0:
            instruction_counter -= 1
            if direction == 'R':
                if x+1 == 150 or map[y][x+1] == ' ':
                    new_x, new_y, new_direction = x_boundaries[y][1]
                    if map[new_y][new_x] != '#':
                        x = new_x
                        y = new_y
                        direction = new_direction
                    else:
                        instruction_counter = 0
                elif map[y][x+1] == '#':
                    instruction_counter = 0
                else:
                    x += 1
            elif direction == 'D':
                if y+1 == 200 or map[y+1][x] == ' ':
                    new_x, new_y, new_direction = y_boundaries[x][1]
                    if map[new_y][new_x] != '#':
                        x = new_x
                        y = new_y
                        direction = new_direction
                    else:
                        instruction_counter = 0
                elif map[y+1][x] == '#':
                    instruction_counter = 0
                else:
                    y += 1
            elif direction == 'L':
                if x-1 == -1 or map[y][x-1] == ' ':
                    new_x, new_y, new_direction = x_boundaries[y][0]
                    if map[new_y][new_x] != '#':
                        x = new_x
                        y = new_y
                        direction = new_direction
                    else:
                        instruction_counter = 0
                elif map[y][x-1] == '#':
                    instruction_counter = 0
                else:
                    x -= 1
            elif direction == 'U':
                if y-1 == -1 or map[y-1][x] == ' ':
                    new_x, new_y, new_direction = y_boundaries[x][0]
                    if map[new_y][new_x] != '#':
                        x = new_x
                        y = new_y
                        direction = new_direction
                    else:
                        instruction_counter = 0
                elif map[y-1][x] == '#':
                    instruction_counter = 0
                else:
                    y -= 1
            else:
                raise Exception("ill try anything once")
        current_pos = (x, y)
    else:
        if direction == 'R' and instruction == 'R':
            direction = 'D'
        elif direction == 'R' and instruction == 'L':
            direction = 'U'
        elif direction == 'U' and instruction == 'R':
            direction = 'R'
        elif direction == 'U' and instruction == 'L':
            direction = 'L'
        elif direction == 'L' and instruction == 'R':
            direction = 'U'
        elif direction == 'L' and instruction == 'L':
            direction = 'D'
        elif direction == 'D' and instruction == 'R':
            direction = 'L'
        elif direction == 'D' and instruction == 'L':
            direction = 'R'
        else:
            raise Exception("POG")

# print_map(map, current_pos, direction)
print(direction, current_pos)

direction_number = None
if direction == 'R':
    direction_number = 0
elif direction == 'D':
    direction_number = 1
elif direction == 'L':
    direction_number = 2
elif direction == 'U':
    direction_number = 3

print(1000*26 + 4*92, direction_number)
print(map_width, len(map))

map_file.close()
result = 1000 * (current_pos[1] + 1) + 4 * (current_pos[0]+1) + direction_number
print("Result: {}".format(result))
