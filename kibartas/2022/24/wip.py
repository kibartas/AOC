from collections import defaultdict, deque
from copy import deepcopy
from itertools import chain
from time import time
import functools
from math import sqrt

start_time = time()

map = open('input.txt', 'r').read().strip().splitlines()

first_blizzard = None
historical_blizzards = []
arrows = defaultdict(lambda: [])
for y, line in enumerate(map):
    map[y] = list(map[y])
    for x, char in enumerate(map[y]):
        if char == '>':
            arrows['>'].append((x, y))
        elif char == '<':
            arrows['<'].append((x, y))
        elif char == '^':
            arrows['^'].append((x, y))
        elif char == 'v':
            arrows['v'].append((x, y))

start = (map[0].index('.'), 0)
goal = (len(map[0])-2, len(map)-2)


def move_blizzards():
    # historical_blizzards.append(arrows.copy())
    for direction in arrows.keys():
        if direction == '<':
            for i in range(len(arrows[direction])):
                arrows[direction][i] = (arrows[direction][i][0] - 1, arrows[direction][i][1])
                if arrows[direction][i][0] == 0:
                    arrows[direction][i] = (len(map[0]) - 2, arrows[direction][i][1])
        elif direction == '>':
            for i in range(len(arrows[direction])):
                arrows[direction][i] = (arrows[direction][i][0] + 1, arrows[direction][i][1])
                if arrows[direction][i][0] == len(map[0]) - 1:
                    arrows[direction][i] = (1, arrows[direction][i][1])
        elif direction == '^':
            for i in range(len(arrows[direction])):
                arrows[direction][i] = (arrows[direction][i][0], arrows[direction][i][1] - 1)
                if arrows[direction][i][1] == 0:
                    arrows[direction][i] = (arrows[direction][i][0], len(map) - 2)
        elif direction == 'v':
            for i in range(len(arrows[direction])):
                arrows[direction][i] = (arrows[direction][i][0], arrows[direction][i][1] + 1)
                if arrows[direction][i][1] == len(map) - 1:
                    arrows[direction][i] = (arrows[direction][i][0], 1)


def print_map():
    for y, _ in enumerate(map):
        for x, _ in enumerate(map[y]):
            chosen_dir = None
            for direction in arrows.keys():
                if [x, y] in arrows[direction]:
                    if chosen_dir is not None:
                        if isinstance(chosen_dir, int):
                            chosen_dir += 1
                        else:
                            chosen_dir = 2
                    else:
                        chosen_dir = direction
            if chosen_dir is None:
                if map[y][x] == '#':
                    print('#', end='')
                else:
                    print('.', end='')
            else:
                print(chosen_dir, end='')
        print()
    print('\n\n')

def get_blizzards():
    while True:
        move_blizzards() 
        if arrows == first_blizzard:
            break
        historical_blizzards.append(set(list(chain(*deepcopy(list(arrows.values()))))))

def get_candidates(goal, blizzards, from_i):
    x, y = goal
    candidates = defaultdict(lambda: [])
    i = from_i + 1
    while i != from_i:
        # print(blizzards[i], [x, y-1])
        if y-1 > 0 and map[y-1][x] != '#' and [x, y-1] not in blizzards[i]:
            candidates[(x, y-1)].append(i)
        if y+1 < len(map)-1 and map[y+1][x] != '#' and [x, y+1] not in blizzards[i]:
            candidates[(x, y+1)].append(blizzards[i])
        if x-1 > 0 and map[y][x-1] != '#' and [x-1, y] not in blizzards[i]:
            candidates[(x-1, y)].append(i)
        if x+1 < len(map[0])-1 and map[y][x+1] != '#' and [x+1, y] not in blizzards[i]:
            candidates[(x+1, y)].append(blizzards[i])
        i += 1
        i %= len(blizzards)
    return candidates

# def traverse_back(start, goal, historical_blizz):
#     # candidates = {}
#     candidates = get_candidates(goal, historical_blizz)
#     print(goal, len(candidates.values()))
#     if goal == start:
#         exit()
#     for next_goal in candidates.keys():
#         traverse_back(start, next_goal, candidates[next_goal])


first_blizzard = deepcopy(arrows)
print(list(chain(*deepcopy(list(arrows.values())))))
historical_blizzards.append(set(list(chain(*deepcopy(list(arrows.values()))))))
get_blizzards()
print(len(historical_blizzards))

every_space = defaultdict(lambda: [])
for y in range(1, len(map)-1):
    for x in range(1, len(map[0])-1):
        for i, hb in enumerate(historical_blizzards):
            if (x, y) not in hb:
                every_space[(x, y)].append(i)
print(every_space)

@functools.cache
def get_next_nodes(current_node):
    next_nodes = set()
    x, y, time = current_node
    every_space_for_current_node = every_space[(x, y)]
    time_index = every_space_for_current_node.index(time)
    i = (time_index + 1) % len(every_space_for_current_node)
    time_cap = every_space_for_current_node[time_index]
    while i != time_index:
        if every_space_for_current_node[i-1] - every_space_for_current_node[i] != -1:
            break
        time_cap = every_space_for_current_node[i]
        i = (i + 1) % len(every_space_for_current_node)
    time_cap = (time_cap + 1) % len(historical_blizzards)
    i = (time+1) % len(historical_blizzards)
    while i != (time_cap + 1) % len(historical_blizzards):
        if y + 1 < len(map)-1 and i in every_space[(x, y+1)]:
            next_nodes.add((x, y+1, i))
        if y - 1 >= 1 and i in every_space[(x, y-1)]:
            next_nodes.add((x, y-1, i))
        if x - 1 >= 1 and i in every_space[(x-1, y)]:
            next_nodes.add((x-1, y, i))
        if x + 1 < len(map[0])-1 and i in every_space[(x+1, y)]:
            next_nodes.add((x+1, y, i))
        i = (i + 1) % len(historical_blizzards)
    return next_nodes

def h(position, goal):
    return abs(position[0] - goal[0]) + abs(position[1] - goal[1])

def get_d(current_node, next_node):
    return next_node[2] - current_node[2]

def a_star(goal, start):
    open_set = {start}
    came_from = {}
    g_score = defaultdict(lambda: float('inf'))
    g_score[start] = 0

    f_score = defaultdict(lambda: float('inf'))
    f_score[start] = h(start, goal)
    
    while len(open_set) != 0:
        current = min(f_score, key=f_score.get)
        if (current[0], current[1]) == goal:
            return came_from, current
        
        if current in open_set:
            open_set.remove(current)
            f_score[current] = float('inf')
        
        next_nodes = get_next_nodes(current)

        for next_node in next_nodes:
            tentative_g_score = g_score[current] + get_d(current, next_node)
            if tentative_g_score < g_score[next_node]:
                came_from[next_node] = current
                g_score[next_node] = tentative_g_score
                f_score[next_node] = tentative_g_score + h(next_node, goal)
                if next_node not in open_set:
                    open_set.add(next_node)
    return 0

# def breadth_first(goal, root):
#     q = deque()
#     explored = {root}
#     parents = {}
#     q.append(root)
#     while len(q) != 0:
#         current_node = q.popleft()
#         if (current_node[0], current_node[1]) == goal:
#             return parents, current_node
#         next_nodes = get_next_nodes(current_node)
#         for next_node in next_nodes:
#             if next_node not in explored:
#                 explored.add(next_node)
#                 parents[next_node] = current_node
#                 q.append(next_node)

# print(every_space)
# for y in range(1, len(map)-1):
#     for x in range(1, len(map[0])-1):
#         print(x, y)
#         # if (x, y) == (6, 4):
#         #     continue
#         space_of_interest = (x, y)
#         other_spaces_of_interest = set()
#         if y + 1 < len(map)-1:
#             other_spaces_of_interest.add((x, y+1))
#         if y - 1 >= 1:
#             other_spaces_of_interest.add((x, y-1))
#         if x - 1 >= 1:
#             other_spaces_of_interest.add((x-1, y))
#         if x + 1 < len(map[0])-1:
#             other_spaces_of_interest.add((x+1, y))
#         for other_space_of_interest in other_spaces_of_interest:
#             for other_space in every_space[other_space_of_interest]:
#                 for j, space in enumerate(every_space[space_of_interest]):
#                     i = space
#                     k = j
#                     valid = False
#                     while True:
#                         if i == other_space:
#                             pass
#                             # print(space_of_interest, other_space_of_interest, space, other_space)
#                         elif every_space[space_of_interest][(k+1) % len(every_space[space_of_interest])] - every_space[space_of_interest][k] != 1:
#                             break
#                         i += 1
#                         k += 1
#                         k %= len(every_space[space_of_interest])
#                         i %= len(historical_blizzards)
#                         if (i+1) % len(historical_blizzards) == space:
#                             break
#                     if valid:
#                         print(space_of_interest, other_space_of_interest, space, other_space)

# 1, 2 -> 1, 1

results, current_node = None, None
the_time = None
end_time = None
to_goal_min_results_counter = float('inf')
for sometime in every_space[(1, 1)]:
    print(sometime)
    the_time = sometime
    something = a_star(goal, (1, 1, sometime))
    if something != 0:
        results, current_node = something
        end_time = current_node[2]
        results_counter = 0
        while current_node != (1, 1, sometime):
            if results[current_node][2] > current_node[2]:
                results_counter += (current_node[2] - results[current_node][2]) % len(historical_blizzards)
            else:
                results_counter += abs(results[current_node][2] - current_node[2])
            current_node = results[current_node]
        results_counter += current_node[2] + 1
        if results_counter < to_goal_min_results_counter:
            to_goal_min_results_counter = results_counter
        break
print("DONE")
end_time_index = every_space[goal].index(end_time)
i = end_time_index + 1
to_start_min_results_counter = float('inf')
sstart_time = None
while i != end_time_index:
    sometime = every_space[goal][i]
    the_time = sometime
    print(goal)
    something = a_star((1, 1), (goal[0], goal[1], sometime))
    if something != 0:
        results, current_node = something
        sstart_time = current_node[2]
        results_counter = 0
        while current_node != (goal[0], goal[1], sometime):
            print(current_node)
            if results[current_node][2] > current_node[2]:
                results_counter += (current_node[2] - results[current_node][2]) % len(historical_blizzards)
            else:
                results_counter += abs(results[current_node][2] - current_node[2])
            current_node = results[current_node]
        results_counter += (current_node[2] - end_time) % len(historical_blizzards)
        print(current_node)
        if results_counter < to_start_min_results_counter:
            to_start_min_results_counter = results_counter
        break
    i = (i + 1) % len(every_space[goal])

sstart_time_index = every_space[(1, 1)].index(sstart_time)
i = sstart_time_index + 1
to_goal_again_min_results_counter = float('inf')
while i != sstart_time_index:
    sometime = every_space[(1, 1)][i]
    the_time = sometime
    something = a_star((goal[0], goal[1]), (1, 1, sometime))
    if something != 0:
        results, current_node = something
        results_counter = 0
        while current_node != (1, 1, sometime):
            if results[current_node][2] > current_node[2]:
                results_counter += (current_node[2] - results[current_node][2]) % len(historical_blizzards)
            else:
                results_counter += abs(results[current_node][2] - current_node[2])
            current_node = results[current_node]
        results_counter += (current_node[2] - sstart_time) % len(historical_blizzards)
        if results_counter < to_goal_again_min_results_counter:
            to_goal_again_min_results_counter = results_counter
        break
    i = (i + 1) % len(every_space[goal])

print(to_goal_min_results_counter, to_start_min_results_counter, to_goal_again_min_results_counter)

result = to_goal_min_results_counter + to_start_min_results_counter + to_goal_again_min_results_counter
print("Result: {}, time: {}s".format(result, time() - start_time))
