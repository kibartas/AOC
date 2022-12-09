input = open('input.txt', 'r').read().strip().splitlines()

visited_positions = set()

positions = {}
for i in range(0, 10):
    positions[i] = [0, 0]
print(positions)
dimensions = 30


direction_map = {'R': (0, 1, 1), 'L': (0, 1, -1), 'U': (1, 0, 1), 'D': (1, 0, -1)}

def print_bridge():
    for i in reversed(range(dimensions)):
        for j in range(dimensions):
            printed = False
            for name, position in positions.items():
                if position[0] == j and position[1] == i:
                    print(name, end='')
                    printed = True
                    break
            if not printed:
                print('.', end='')
        print()
    print('\n\n')


def write_bridge():
    with open('bridge.txt', 'a') as bridge_file:
        for i in reversed(range(dimensions)):
            for j in range(dimensions):
                printed = False
                for name, position in positions.items():
                    if position[0] == j and position[1] == i:
                        bridge_file.write(str(name))
                        printed = True
                        break
                if not printed:
                    bridge_file.write('.')
            bridge_file.write('\n')
        bridge_file.write('\n\n')

def move(direction, count):
    one, _, dir = direction_map[direction] 
    n = 0
    while n < int(count):
        n += 1
        positions[0][one] += 1 * dir
        # # if they were in the same spot, do nothing
        # if t_position[0] + 1 == h_position[0] and t_position[1] == h_position[1]:
        #     continue
        for i in range(1, 10):
            for first, second, directionality in direction_map.values():
                if positions[i][first] + (2 * directionality) == positions[i-1][first] and positions[i][second] == positions[i-1][second]:
                    positions[i][first] += 1 * directionality
                    break
                elif positions[i][first] + (2 * directionality) == positions[i-1][first] and positions[i][second] + 1 == positions[i-1][second]:
                    positions[i][first] += 1 * directionality
                    positions[i][second] += 1
                    break
                elif positions[i][first] + (2 * directionality) == positions[i-1][first] and positions[i][second] - 1 == positions[i-1][second]:
                    positions[i][first] += 1 * directionality
                    positions[i][second] -= 1
                    break
                elif positions[i][first] + (2 * directionality) == positions[i-1][first] and positions[i][second] - 2 == positions[i-1][second]:
                    positions[i][first] += 1 * directionality
                    positions[i][second] -= 1
                    break
                elif positions[i][first] + (2 * directionality) == positions[i-1][first] and positions[i][second] + 2 == positions[i-1][second]:
                    positions[i][first] += 1 * directionality
                    positions[i][second] += 1
                    break
        visited_positions.add(tuple(positions[9]))
    # write_bridge()


print_bridge()
for line in input:
    direction, count = line.split()
    move(direction, count)
            

            
result = len(visited_positions)
print("Result: {}".format(result))
