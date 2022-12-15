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

cannot_be_in = set()
y_of_interest = 2000000

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
    for x in range(sensor[0] - far_from_y, sensor[0] + far_from_y):
        cannot_be_in.add(x)


result = len(cannot_be_in)
print("Result: {}".format(result))
