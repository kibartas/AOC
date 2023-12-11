input = open('input.txt', 'r').read().strip().split('\n')
result = open('result.txt', 'w')
def print_result(expanded_matrix):
    for line in expanded_matrix:
        for el in line:
            result.write(el)
        result.write('\n')
    result.write('\n\n')

expanded_y = set()
expanded_x = set()
# for i, line in enumerate(input):
#     if all([x == '.' for x in line]):
#         for x in range(len(input[0])):
#             if x not in expanded_x and all([input[y][x] == '.' for y in range(len(input))]):
#                 expanded_x.add(x)
#                 expanded_x.add(x+1)
#                 for y in range(len(input)):
#                     input[y] = input[y][:x] + '.' + input[y][x:]
#             if i not in expanded_y and all([input[y][x] == '.' for y in range(len(input))]):
#                 input = input[:i+1] + ['.' * len(input[0])] + input[i+1:]
#                 expanded_y.add(i)

new_lines = []
for line in input:
    new_lines.append(line)
    if '#' not in line:
        new_lines.append(line)

new_lines = list(zip(*new_lines))

the_lines = []
for line in new_lines:
    the_lines.append(line)
    if '#' not in line:
        the_lines.append(line)

the_lines = list(zip(*the_lines))

galaxies = []
for y, line in enumerate(the_lines):
    for x, el in enumerate(the_lines[y]):
        if el == '#':
            galaxies.append((y, x))

def find_path(start, end):
    y_s, x_s = start
    y_e, x_e = end
    return abs(y_e - y_s) + abs(x_e - x_s)

paths_sum = 0
for current_galaxy in range(len(galaxies)-1):
    for other_galaxy in range(current_galaxy+1, len(galaxies)):
        paths_sum += find_path(galaxies[current_galaxy], galaxies[other_galaxy])




print_result(the_lines)

result = paths_sum
print("Result: {}".format(result))
