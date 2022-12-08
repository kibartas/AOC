import copy
import sys
import heapq

input = open('input.txt', 'r').read().strip().split('\n')

out_matrix = []

sys.setrecursionlimit(20000)

big_matrix = open("bigFile.txt", "w")
for line in input:
    out_matrix.append([int(x) for x in list(line)])

middle_matrix = copy.deepcopy(out_matrix)

for j in range(1, 5):
    for i in range(len(out_matrix)):
        middle_matrix.append([(x+j-1) % 9 + 1 for x in out_matrix[i]])

final_matrix = copy.deepcopy(middle_matrix)

for i in range(0, len(middle_matrix)):
    for j in range(1, 5):
        final_matrix[i] += [(x+j-1) % 9 + 1 for x in middle_matrix[i]]
    big_matrix.write(''.join([str(x) for x in final_matrix[i]]))
    big_matrix.write('\n')


def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from.keys():
        current = came_from[current]
        total_path.append(current)
    return total_path


def a_star(start, goal, h):
    open_set = [start]

    heapq.heapify(open_set)

    came_from = {}

    g_score = {}
    g_score[start] = 0

    f_score = {}
    f_score[start] = h[start]

    while len(open_set) > 0:
        current = heapq.heappop(open_set)

        if current == goal:
            return reconstruct_path(came_from, current)

        (x, y) = current
        for neighbor in [(x, y+1), (x, y-1), (x+1, y), (x-1, y)]:
            if neighbor[0] < 0 or neighbor[0] == len(final_matrix) or neighbor[1] < 0 or neighbor[1] == len(final_matrix):
                continue

            tentative_g_score = g_score[current] + \
                final_matrix[neighbor[0]][neighbor[1]]
            if tentative_g_score < g_score.get(neighbor, 10e5):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + h[neighbor]

                if neighbor not in open_set:
                    heapq.heappush(open_set, neighbor)
    return "FISH"


memoized = {}
matrix = final_matrix


def calculate_score(path):
    sum_of = 0
    path = path[:-1]
    for pair in path:
        sum_of += matrix[pair[0]][pair[1]]
    return sum_of


C = len(matrix)*len(matrix)
for i in range(len(matrix)):
    for j in range(len(matrix)):
        memoized[(i, j)] = C - i - j
best_path = a_star((0, 0), (len(final_matrix)-1,
                            len(final_matrix)-1), memoized)
result = calculate_score(best_path)
print("Result: {}".format(result))
