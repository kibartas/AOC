import string
from collections import defaultdict
from math import sqrt
import time

input = open('input.txt', 'r').read().strip().splitlines()

height_map = {letter: ord(letter) for letter in string.ascii_lowercase}

height_map['E'] = ord('z')
height_map['S'] = ord('a')

e_pos = None
s_pos = None

for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] == 'E':
            e_pos = (j, i)
        if input[i][j] == 'S':
            s_pos = (j, i)

def h(position):
    return round(sqrt(abs(position[0] - e_pos[0]) + abs(position[1] - e_pos[1])))


def get_height(letter):
    return height_map[letter]

def get_d(current, next):
    return 1

def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from.keys():
        current = came_from[current]
        total_path.insert(0, current)
    return total_path


def a_star(start, goal, h):
    open_set = {start}
    came_from = {}
    g_score = defaultdict(lambda: float('inf'))
    g_score[start] = 0

    f_score = defaultdict(lambda: float('inf'))
    f_score[start] = h(start)
    
    while len(open_set) != 0:
        current = min(f_score, key=f_score.get)
        if current == goal:
            return reconstruct_path(came_from, current)
        
        # print(open_set)
        
        # print(current, f_score[current], min(f_score.values()))
        if current in open_set:
            open_set.remove(current)
            f_score[current] = float('inf')
        
        climbable = get_climbable_blocks(current)

        for neighbor in climbable:
            tentative_g_score = g_score[current] + get_d(current, neighbor)
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + h(neighbor)
                if neighbor not in open_set:
                    open_set.add(neighbor)
    return "WAT"

def get_climbable_blocks(position):
    x, y = position
    current_height = get_height(input[y][x])
    climbable_blocks = []
    if len(input[y]) - 1 != x and current_height + 1 >= get_height(input[y][x+1]):
        climbable_blocks.append((x+1, y))
    if x != 0 and current_height + 1 >= get_height(input[y][x-1]):
        climbable_blocks.append((x-1, y))

    if len(input) - 1 != y and current_height + 1 >= get_height(input[y + 1][x]):
        climbable_blocks.append((x, y+1))
    if y != 0 and current_height + 1 >= get_height(input[y-1][x]):
        climbable_blocks.append((x, y-1))
    return climbable_blocks


def climb_mountain(position, visited_blocks=set()):
    x, y = position
    if input[y][x] == 'E':
        return len(visited_blocks)
    visited_blocks = visited_blocks | {(position)}
    # climbable = get_climbable_blocks(position)
    # if x == 6 and y == 0:
    #     print(position, climbable, visited_blocks)
    all_results = []
    for next_pos in climbable:
        if next_pos in visited_blocks:
            continue
        all_results.append(climb_mountain(next_pos, visited_blocks))
    # print(all_results)
    return min(all_results) if len(all_results) != 0 else 1000


result = len(a_star(s_pos, e_pos, h)) - 1

print("Result: {}".format(result))
