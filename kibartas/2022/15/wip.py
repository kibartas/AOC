from time import time

input = open('input.txt', 'r').read().strip().splitlines()
s_and_b = {}

def get_distance(a, b):
    x_1, y_1 = a
    x_2, y_2 = b
    return abs(x_1 - x_2) + abs(y_1 - y_2)

def get_area(distance):
    return ((distance * 2) + 1) * (distance + 1) - (distance) - 2 # -2 is sensor and beacon

for line in input:
    elements = line.split()
    _, x = elements[2].split('=')
    x = int(x[:-1])
    _, y = elements[3].split('=')
    y = int(y[:-1])
    _, b_x = elements[-2].split('=')
    b_x = int(b_x[:-1])
    _, b_y = elements[-1].split('=')
    b_y = int(b_y)

    s = (x, y)
    b = (b_x, b_y)
    distance = get_distance(s, b)
    area = get_area(distance)
    s_and_b[(x, y)] = (b_x, b_y, distance, area)

print(s_and_b)

constraint = 4000000

for y_of_interest in range(constraint + 1):
    # time_for_cycle_start = time()
    # print(y_of_interest)
    cannot_be_in_bounds = []
    for sensor, beacon in s_and_b.items():
        distance = beacon[2]
        if sensor[1] < y_of_interest and sensor[1] + distance >= y_of_interest:
            abs_distance = sensor[1] + distance
            far_from_y = abs(abs_distance - y_of_interest)
        elif sensor[1] > y_of_interest and sensor[1] - distance <= y_of_interest:
            abs_distance = sensor[1] - distance
            far_from_y = abs(abs_distance - y_of_interest)
        elif sensor[1] == y_of_interest:
            far_from_y = distance
        else:
            continue
        one_line_area = 2 * far_from_y + 1
        cannot_be_in_bounds.append((max(sensor[0] - far_from_y, 0), min(sensor[0] + far_from_y, constraint + 1)))

    i = 0
    cannot_be_in_bounds.sort(key=lambda x: x[0])
    while i < len(cannot_be_in_bounds) - 1:
        j = i+1
        if i == 0 and cannot_be_in_bounds[i][0] != 0:
            print('GOTEM', cannot_be_in_bounds)
            distress = (0, y_of_interest)
        elif cannot_be_in_bounds[i][1] >= cannot_be_in_bounds[j][1]:
            while j < len(cannot_be_in_bounds) and cannot_be_in_bounds[i][1] > cannot_be_in_bounds[j][1]:
                j += 1
            i = j - 1
        elif cannot_be_in_bounds[i][1] + 2 == cannot_be_in_bounds[j][0]:
            print('GOTEM', cannot_be_in_bounds)
            distress = (cannot_be_in_bounds[i][1]+1, y_of_interest)
        elif j == len(cannot_be_in_bounds) - 1 and cannot_be_in_bounds[j][1] < constraint:
            print('GOTEM', cannot_be_in_bounds)
            distress = (constraint, y_of_interest)

        
        i += 1


result = distress[0] * constraint + distress[1]
print("Result: {}".format(result))
