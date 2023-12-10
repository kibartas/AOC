from copy import deepcopy
import sys

sys.setrecursionlimit(10000)

input = open('input.txt', 'r').read().strip().split('\n')

pipes = {'|': (1, 0, 1, 0), '-': (0, 1, 0, 1), 'L': (1, 1, 0, 0), 'J': (1, 0, 0, 1), '7': (0, 0, 1, 1), 'F': (0, 1, 1, 0)}
start_point = 'S'
ground = '.'

start_coords = None
for y, line in enumerate(input):
    found = False
    for x, el in enumerate(line):
        if el == start_point:
            start_coords = (y, x)
            found = True
            break
    if found:
        break


def find_candidates(depth, start_coords, visited_tiles):
    candidates = {}
    for y in (1, -1):
        y_s, x_s = start_coords
        y_s += y
        if y_s >= len(input) or y_s < 0 or input[y_s][x_s] == '.' or (y_s, x_s) in visited_tiles:
            continue
        if y == 1 and (input[y_s - y][x_s] == 'S' or pipes[input[y_s - y][x_s]][2]) and pipes[input[y_s][x_s]][0]:
            candidates[(y_s, x_s)] = depth
        elif y == -1 and (input[y_s - y][x_s] == 'S' or pipes[input[y_s - y][x_s]][0]) and pipes[input[y_s][x_s]][2]:
            candidates[(y_s, x_s)] = depth

    for x in (1, -1):
        y_s, x_s = start_coords
        x_s += x
        if x_s >= len(input[0]) or x_s < 0 or input[y_s][x_s] == '.' or (y_s, x_s) in visited_tiles:
            continue
        if x == 1 and (input[y_s][x_s - x] == 'S' or pipes[input[y_s][x_s - x]][1]) and pipes[input[y_s][x_s]][3]:
            candidates[(y_s, x_s)] = depth
        elif x == -1 and (input[y_s][x_s - x] == 'S' or pipes[input[y_s][x_s - x]][3]) and pipes[input[y_s][x_s]][1]:
            candidates[(y_s, x_s)] = depth
    return candidates

visited_tiles = {start_coords: 0}
candidates_to_check = list(visited_tiles)
i = 1
while len(candidates_to_check) > 0:
    new_candidates_to_check = []
    for candidate in candidates_to_check:
        new_candidates = find_candidates(i, candidate, visited_tiles)
        new_candidates_to_check += list(new_candidates)
        visited_tiles |= new_candidates
    candidates_to_check = new_candidates_to_check
    i += 1

result = open('result.txt', 'w')
def print_result(expanded_matrix):
    for line in expanded_matrix:
        for el in line:
            result.write(el)
        result.write('\n')
    result.write('\n\n')
expanded_matrix = []
for y in range(len(input)):
    expanded_matrix.append([])
    for x in range(len(input[0])):
        if (y, x) not in visited_tiles:
            expanded_matrix[y].append('.')
        # Hack time
        elif input[y][x] == 'S':
            expanded_matrix[y].append('7')
        else:
            expanded_matrix[y].append(input[y][x])

print_result(expanded_matrix)

def can_expand(y, x, expanded_matrix):
    if x+1 == len(expanded_matrix[0]):
        return False
    first_el, second_el = expanded_matrix[y][x], expanded_matrix[y][x+1]
    return ((first_el == '|' and second_el == '|') or 
            (first_el == '|' and second_el == 'F') or 
            (first_el == '|' and second_el == 'L') or 
            (first_el == 'J' and second_el == 'L') or 
            (first_el == 'J' and second_el == 'F') or 
            (first_el == 'J' and second_el == '|') or
            (first_el == '7' and second_el == 'F') or
            (first_el == '7' and second_el == 'L') or
            (first_el == '7' and second_el == '|'))

def can_expand_y(y, x, expanded_matrix):
    if y+1 == len(expanded_matrix):
        return False
    first_el, second_el = expanded_matrix[y][x], expanded_matrix[y+1][x]
    return ((first_el == '-' and second_el == '-') or 
            (first_el == '-' and second_el == 'F') or 
            (first_el == '-' and second_el == '7') or 
            (first_el == 'J' and second_el == 'F') or 
            (first_el == 'J' and second_el == '7') or 
            (first_el == 'J' and second_el == '-') or
            (first_el == 'L' and second_el == '-') or
            (first_el == 'L' and second_el == 'F') or
            (first_el == 'L' and second_el == '7'))

def can_expand_y_el(first_el, second_el, expanded_matrix):
    return ((first_el == '-' and second_el == '-') or 
            (first_el == '-' and second_el == 'F') or 
            (first_el == '-' and second_el == '7') or 
            (first_el == 'J' and second_el == 'F') or 
            (first_el == 'J' and second_el == '7') or 
            (first_el == 'J' and second_el == '-') or
            (first_el == 'L' and second_el == '-') or
            (first_el == 'L' and second_el == 'F') or
            (first_el == 'L' and second_el == '7'))

x = 0
while x < len(expanded_matrix[0]):
    for y in range(len(input)):
        if can_expand(y, x, expanded_matrix):
            all_expanded = True
            temp_expanded_matrix = deepcopy(expanded_matrix)
            temp_expanded_matrix[y] = temp_expanded_matrix[y][:x+1] + ['X'] + temp_expanded_matrix[y][x+1:]
            for y in range(len(input)):
                if temp_expanded_matrix[y][x+1] == 'X':
                    continue
                expanded = False
                if temp_expanded_matrix[y][x+1] == '-':
                    expanded = True
                    temp_expanded_matrix[y] = temp_expanded_matrix[y][:x+1] + ['_'] + temp_expanded_matrix[y][x+1:]
                if temp_expanded_matrix[y][x+1] == '.':
                    expanded = True
                    temp_expanded_matrix[y] = temp_expanded_matrix[y][:x+1] + ['X'] + temp_expanded_matrix[y][x+1:]
                if can_expand(y, x, temp_expanded_matrix):
                    expanded = True
                    temp_expanded_matrix[y] = temp_expanded_matrix[y][:x+1] + ['X'] + temp_expanded_matrix[y][x+1:]

                if not expanded and temp_expanded_matrix[y][x+1] != 'X':
                    if temp_expanded_matrix[y][x] == '.':
                        expanded = True
                        temp_expanded_matrix[y] = temp_expanded_matrix[y][:x+1] + ['X'] + temp_expanded_matrix[y][x+1:]
                    if temp_expanded_matrix[y][x] == '-':
                        expanded = True
                        temp_expanded_matrix[y] = temp_expanded_matrix[y][:x+1] + ['_'] + temp_expanded_matrix[y][x+1:]
                    if not expanded:
                        expanded = True
                        temp_expanded_matrix[y] = temp_expanded_matrix[y][:x+1] + ['_'] + temp_expanded_matrix[y][x+1:]
                if not expanded:
                    all_expanded = False
                    break

            if all_expanded:
                expanded_matrix = temp_expanded_matrix
                        
            break
    x += 1

for y in range(len(expanded_matrix)):
    for x in range(len(expanded_matrix[y])):
        if expanded_matrix[y][x] == '_':
            expanded_matrix[y][x] = '-'
print_result(expanded_matrix)

y = 0
while y < len(expanded_matrix):
    for x in range(len(expanded_matrix[0])):
        if can_expand_y(y, x, expanded_matrix):
            print('can_expand_y', y, x)
            all_expanded = True
            temp_expanded_matrix = deepcopy(expanded_matrix)
            temp_expanded_matrix = temp_expanded_matrix[:y+1] + ['X'] + temp_expanded_matrix[y+1:]
            temp_expanded_matrix[y+1] = ['X'] * x + ['X'] + ['X'] * (len(expanded_matrix[0]) - x - 1)
            for x in range(len(expanded_matrix[0])):
                if temp_expanded_matrix[y][x] == 'X':
                    continue
                expanded = False
                if temp_expanded_matrix[y][x] == '|':
                    expanded = True
                    temp_expanded_matrix[y+1][x] = '|'
                if temp_expanded_matrix[y][x] == '.':
                    expanded = True
                    temp_expanded_matrix[y+1][x] = 'X'
                if can_expand_y_el(temp_expanded_matrix[y][x], temp_expanded_matrix[y+2][x], temp_expanded_matrix):
                    expanded = True
                    temp_expanded_matrix[y+1][x] = 'X'

                if not expanded:
                    if temp_expanded_matrix[y+2][x] == '.' or temp_expanded_matrix[y+2][x] == 'X':
                        expanded = True
                        temp_expanded_matrix[y+1][x] = 'X'
                    if temp_expanded_matrix[y+2][x] == '|':
                        expanded = True
                        temp_expanded_matrix[y+1][x] = '|'
                    if not expanded:
                        expanded = True
                        temp_expanded_matrix[y+1][x] = '|'
                # if not expanded:
                #     all_expanded = False
                #     break
            

            if all_expanded:
                expanded_matrix = temp_expanded_matrix
                        
            break
    y += 1

for y in range(len(expanded_matrix)):
    for x in range(len(expanded_matrix[y])):
        if expanded_matrix[y][x] == '_':
            expanded_matrix[y][x] = '-'

print_result(expanded_matrix)

def flood(y, x, flooded_matrix, flood_set):
    flood_set.add((y, x))
    if x + 1 < len(flooded_matrix[0]):
        next_x_el = flooded_matrix[y][x+1]
        if (next_x_el == '.' or next_x_el == 'X') and (y, x+1) not in flood_set:
            flood_set = flood_set.union(flood(y, x+1, flooded_matrix, flood_set))
    if x - 1 >= 0:
        next_x_el = flooded_matrix[y][x-1]
        if (next_x_el == '.' or next_x_el == 'X') and (y, x-1) not in flood_set:
            flood_set = flood_set.union(flood(y, x-1, flooded_matrix, flood_set))
    if y + 1 < len(flooded_matrix):
        next_y_el = flooded_matrix[y+1][x]
        if (next_y_el == '.' or next_y_el == 'X') and (y+1, x) not in flood_set:
            flood_set = flood_set.union(flood(y+1, x, flooded_matrix, flood_set))
    if y - 1 >= 0:
        next_y_el = flooded_matrix[y-1][x]
        if (next_y_el == '.' or next_y_el == 'X') and (y-1, x) not in flood_set:
            flood_set = flood_set.union(flood(y-1, x, flooded_matrix, flood_set))
    return flood_set

flooded_matrix = deepcopy(expanded_matrix)
flood_set = set()
for y in range(len(expanded_matrix)):
    if y == 0 or y == len(expanded_matrix) - 1:
        x_range = range(len(expanded_matrix[0]))
    else:
        x_range = (0, len(expanded_matrix[0]) - 1)
    for x in x_range:
        if flooded_matrix[y][x] == '.' or flooded_matrix[y][x] == 'X':
            flood_set = flood(y, x, flooded_matrix, flood_set)
            for (new_y, new_x) in flood_set:
                flooded_matrix[new_y][new_x] = '+'

print_result(flooded_matrix)

result = 0
for line in flooded_matrix:
    for el in line:
        if el == '.':
            result += 1


print("Result: {}".format(result))

