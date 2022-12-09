input = open('input.txt', 'r').read().strip().splitlines()

visited_positions = set()

h_position = [0, 0]
t_position = [0, 0]

direction_map = {'R': (0, 1, 1), 'L': (0, 1, -1), 'U': (1, 0, 1), 'D': (1, 0, -1)}

def print_bridge():
    for i in reversed(range(5)):
        for j in range(6):
            if h_position[0] == j and h_position[1] == i:
                print('H', end='')
            elif t_position[0] == j and t_position[1] == i:
                print('T', end='')
            else:
                print('.', end='')
        print()
    print('\n\n')

def move(direction, count):
    first, second, directionality = direction_map[direction] 
    n = 0
    while n < int(count):
        n += 1
        h_position[first] += 1 * directionality
        # # if they were in the same spot, do nothing
        # if t_position[0] + 1 == h_position[0] and t_position[1] == h_position[1]:
        #     continue
        if t_position[first] + (2 * directionality) == h_position[first] and t_position[second] == h_position[second]:
            t_position[first] += 1 * directionality
        elif t_position[first] + (2 * directionality) == h_position[first] and t_position[second] + 1 == h_position[second]:
            t_position[first] += 1 * directionality
            t_position[second] += 1
        elif t_position[first] + (2 * directionality) == h_position[first] and t_position[second] - 1 == h_position[second]:
            t_position[first] += 1 * directionality
            t_position[second] -= 1
        # print_bridge()
        visited_positions.add(tuple(t_position))

print_bridge()
for line in input:
    direction, count = line.split()
    move(direction, count)
            

            
result = len(visited_positions)
print("Result: {}".format(result))
