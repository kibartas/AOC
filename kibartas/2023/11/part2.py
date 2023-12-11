input = open('input.txt', 'r').read().strip().split('\n')
result = open('result.txt', 'w')
galaxy_constant = 1000000
def print_result(expanded_matrix):
    for line in expanded_matrix:
        for el in line:
            result.write(el)
        result.write('\n')
    result.write('\n\n')

expanded_y = set()
expanded_x = set()

long_lines_y = []
line_counter_y = 0
new_lines = []
for line in input:
    new_lines.append(line)
    line_counter_y += 1
    if '#' not in line:
        long_lines_y.append(line_counter_y)
        new_lines.append(line)
        line_counter_y += 1

new_lines = list(zip(*new_lines))

long_lines_x = []
line_counter_x = 0
the_lines = []
for line in new_lines:
    the_lines.append(line)
    line_counter_x += 1
    if '#' not in line:
        long_lines_x.append(line_counter_x)
        the_lines.append(line)
        line_counter_x += 1

the_lines = list(zip(*the_lines))

galaxies = []
for y, line in enumerate(the_lines):
    for x, el in enumerate(the_lines[y]):
        if el == '#':
            galaxies.append((y, x))

def find_path(start, end):
    y_s, x_s = start
    y_e, x_e = end
    naive_distance = abs(y_e - y_s) + abs(x_e - x_s)
    for x in range(min(x_s, x_e), max(x_s, x_e)):
        if x in long_lines_x:
            naive_distance += galaxy_constant - 2
    for y in range(min(y_s, y_e), max(y_s, y_e)):
        if y in long_lines_y:
            naive_distance += galaxy_constant - 2
    return naive_distance

paths_sum = 0
for current_galaxy in range(len(galaxies)-1):
    for other_galaxy in range(current_galaxy+1, len(galaxies)):
        paths_sum += find_path(galaxies[current_galaxy], galaxies[other_galaxy])




print_result(the_lines)

result = paths_sum
print("Result: {}".format(result))
