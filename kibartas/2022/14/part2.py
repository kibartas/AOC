from collections import defaultdict

input = open('input.txt', 'r').read().strip().splitlines()


rock_lines = defaultdict(lambda: [])
sand = defaultdict(lambda: [])

biggest_y = 0
for line in input:
    parts = line.split('->')
    for i in range(len(parts)-1):
        x, y = parts[i].split(',')
        next_x, next_y = parts[i+1].split(',')
        x, y, next_x, next_y = int(x), int(y), int(next_x), int(next_y)
        if y > biggest_y:
            biggest_y = y
        if next_y > biggest_y:
            biggest_y = next_y
        if next_x > x:
            while x <= next_x:
                rock_lines[x].append(y)
                x += 1
        elif next_x < x:
            while x >= next_x:
                rock_lines[x].append(y)
                x -= 1
        elif next_y > y:
            while y <= next_y:
                rock_lines[x].append(y)
                y += 1
        elif next_y < y:
            while y >= next_y:
                rock_lines[x].append(y)
                y -= 1
        elif next_x == x and next_y == y:
            raise Exception("SAME SHIT")
        if next_x != x and next_y != y:
            raise Exception("DIAGONAL")


floor = biggest_y + 2

rock_lines = defaultdict(lambda: [floor], rock_lines)
for rock_line in rock_lines.keys():
    rock_lines[rock_line].append(floor)

for rock_line in rock_lines.keys():
    rock_lines[rock_line].sort()

print('floor', floor)

# print(rock_lines)

def drop_sand(drop_from_x, drop_from_y, enable_logging=False):
    if enable_logging:
        print('start', drop_from_x, drop_from_y)
    x_blocker = drop_from_x
    y_blocker_rock = float('inf')
    y_blocker_sand = float('inf')
    if len(rock_lines[drop_from_x]) != 0:
        y_blocker_rock = next((z for z in rock_lines[drop_from_x] if z > drop_from_y), float('inf'))
    if len(sand[drop_from_x]) != 0:
        y_blocker_sand = next((z for z in sand[drop_from_x] if z > drop_from_y), float('inf'))
    y_blocker = min(y_blocker_rock, y_blocker_sand)
    enable_logging = enable_logging or y_blocker == 1
    if 1 in sand[x_blocker - 1] and 1 in sand[x_blocker + 1]:
        return True
    if enable_logging:
        print('after_blocker', x_blocker, y_blocker)
    if y_blocker not in rock_lines[x_blocker - 1] and y_blocker not in sand[x_blocker - 1]:
        if enable_logging:
            return drop_sand(x_blocker-1, y_blocker, True)
        else:
            return drop_sand(x_blocker-1, y_blocker)
    elif y_blocker not in rock_lines[x_blocker + 1] and y_blocker not in sand[x_blocker + 1]:
        if enable_logging:
            return drop_sand(x_blocker+1, y_blocker, True)
        else:
            return drop_sand(x_blocker+1, y_blocker)
    if enable_logging:
        print('end', x_blocker, y_blocker-1) 
    sand[x_blocker].insert(0, y_blocker-1)

x = False
while x != True:
    x = drop_sand(500, 0)

# for i in range(100):
#     for j in range(300, 550):
#         if (j, i) == (500, 0):
#             print('+', end='')
#         elif i in rock_lines[j]:
#             print('#', end='')
#         elif i in sand[j]:
#             print('o', end='')
#         else:
#             print('.', end='')
#     print()

def write_to_file():
    with open('result.txt', 'w') as result_file:
        for i in range(300):
            for j in range(400, 600):
                if (j, i) == (500, 0):
                    result_file.write('+')
                elif i in rock_lines[j]:
                    result_file.write('#')
                elif i in sand[j]:
                    result_file.write('o')
                else:
                    result_file.write('.')
            result_file.write('\n')
write_to_file()
sand_count = 0
for sand_y in sand.values():
    sand_count += len(set(sand_y))
# add the very top too
result = sand_count + 1
print("Result: {}".format(result))
