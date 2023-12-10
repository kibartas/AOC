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
        if y == 1 and pipes[input[y_s][x_s]][0]:
            candidates[(y_s, x_s)] = depth
        elif y == -1 and pipes[input[y_s][x_s]][2]:
            candidates[(y_s, x_s)] = depth

    for x in (1, -1):
        y_s, x_s = start_coords
        x_s += x
        if x_s >= len(input) or x_s < 0 or input[y_s][x_s] == '.' or (y_s, x_s) in visited_tiles:
            continue
        if x == 1 and pipes[input[y_s][x_s]][3]:
            candidates[(y_s, x_s)] = depth
        elif x == -1 and pipes[input[y_s][x_s]][1]:
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

result = max(visited_tiles.values())
print("Result: {}".format(result))