import re
import time

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
map_width = max([len(line) for line in map])

for i in range(len(map)):
    start = re.search(r' [#.]', map[i])
    if start == None:
        start = 0
    else:
        start = start.start() + 1
    end = re.search(r'[#.] ', map[i])
    if end == None:
        end = len(map[i])-1
    else:
        end = end.start()
    x_boundaries[i] = (start, end)
    map[i] = list(map[i])
    if len(map[i]) < map_width:
        map[i] += list(' ' * (map_width-len(map[i])))
    # print(i)
    # x_boundaries[i] = (map[i].index(r' .'), map[i].index(r'. '))
    # print(x_boundaries[i])

y_boundaries = {}
for x in range(map_width):
    first = None
    second = None
    for y in range(len(map)):
        try:
            if first is None and map[y][x] != ' ':
                first = y
            elif first is not None and map[y][x] == ' ':
                second = y - 1
                break
        except:
            if first is not None:
                second = y - 1
                break
            continue
    if second is None:
        second = len(map) - 1
    y_boundaries[x] = (first, second)

print(y_boundaries)

current_pos = (map[0].index('.'), 0)
direction = 'R'
print_map(map, current_pos, direction)

for instruction in instructions_list:
    if isinstance(instruction, int):
        x, y = current_pos
        if direction == 'R':
            for i in range(instruction):
                if x+1 == len(map[y]) or map[y][x+1] == ' ':
                    if map[y][x_boundaries[y][0]] != '#':
                        x = x_boundaries[y][0]
                    else:
                        break
                elif map[y][x+1] == '#':
                    break
                else:
                    x = x+1
        elif direction == 'D':
            for i in range(instruction):
                if y+1 == len(map) or map[y+1][x] == ' ':
                    if map[y_boundaries[x][0]][x] != '#':
                        y = y_boundaries[x][0]
                    else:
                        break
                elif map[y+1][x] == '#':
                    break
                else:
                    y = y+1
        elif direction == 'L':
            for i in range(instruction):
                if x-1 == -1 or map[y][x-1] == ' ':
                    if map[y][x_boundaries[y][1]] != '#':
                        x = x_boundaries[y][1]
                    else:
                        break
                elif map[y][x-1] == '#':
                    break
                else:
                    x = x-1
        elif direction == 'U':
            for i in range(instruction):
                if y-1 == -1 or map[y-1][x] == ' ':
                    if map[y_boundaries[x][1]][x] != '#':
                        y = y_boundaries[x][1]
                    else:
                        print("HELLO")
                        break
                elif map[y-1][x] == '#':
                    break
                else:
                    y = y-1
        else:
            raise Exception("HUH?")
        current_pos = (x, y)
    else:
        if instruction != 'R' and instruction != 'L':
            raise Exception("HUH")
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
    # write_map(map, current_pos, direction)

print_map(map, current_pos, direction)
print(current_pos)

direction_number = None
if direction == 'R':
    direction_number = 0
elif direction == 'D':
    direction_number = 1
elif direction == 'L':
    direction_number = 2
elif direction == 'U':
    direction_number = 3

map_file.close()
result = 1000 * (current_pos[1] + 1) + 4 * (current_pos[0]+1) + direction_number
print("Result: {}".format(result))
