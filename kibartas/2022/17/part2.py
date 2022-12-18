rocks = open('rocks.txt', 'r').read().split('\n\n')
input = open('input.txt', 'r').read().strip()
heights = open('heights.txt', 'r').read().splitlines()
print(rocks)
print(len(input))

chamber_width = 7
chamber_height = 3


def get_rock_start(rock):
    if rock == '####':
        return [(2, chamber_height), (3, chamber_height), (4, chamber_height), (5, chamber_height)], [[0], [3]], [0, [0, 1, 2, 3]]
    elif rock == '.#.\n###\n.#.':
        return [(3, chamber_height+2), (2, chamber_height+1), (3, chamber_height+1), (4, chamber_height+1), (3, chamber_height)], [[0, 1, 4], [0, 3, 4]], [0, [1, 3, 4]]
    elif rock == '..#\n..#\n###':
        return [(4, chamber_height+2), (4, chamber_height+1), (2, chamber_height), (3, chamber_height), (4, chamber_height)], [[0, 1, 2], [0, 1, 4]], [0, [2, 3, 4]]
    elif rock == '#\n#\n#\n#':
        return [(2, chamber_height+3), (2, chamber_height+2), (2, chamber_height+1), (2, chamber_height)], [[0, 1, 2, 3], [0, 1, 2, 3]], [0, [3]]
    elif rock == '##\n##':
        return [(2, chamber_height+1), (3, chamber_height+1), (2, chamber_height), (3, chamber_height)], [[0, 2], [1, 3]], [0, [2, 3]]
    else:
        raise Exception("NO")


        
chamber = set()

def is_touching_left(rock_position, x_bounds_left):
    for x_bound_left in x_bounds_left:
        if rock_position[x_bound_left][0] == 0 or (rock_position[x_bound_left][0] - 1, rock_position[x_bound_left][1]) in chamber:
            return True
    return False

def is_touching_right(rock_position, x_bounds_right):
    for x_bound_right in x_bounds_right:
        if rock_position[x_bound_right][0] + 1 == chamber_width or (rock_position[x_bound_right][0] + 1, rock_position[x_bound_right][1]) in chamber:
            return True
    return False


def push_rock(rock_position, direction, x_bounds):
    # print(x_bounds[1])
    if direction == '>':
        if not is_touching_right(rock_position, x_bounds[1]):
            return [(x+1, y) for (x, y) in rock_position]
        else:
            return rock_position
    elif direction == '<':
        if not is_touching_left(rock_position, x_bounds[0]):
            return [(x-1, y) for (x, y) in rock_position]
        else:
            return rock_position
    else:
        raise Exception("LOL")

def print_chamber(rock_position, rock_symbol='@'):
    global chamber_height
    for chamber_y in reversed(range(chamber_height+1)):
        for chamber_x in range(chamber_width):
            if (chamber_x, chamber_y) in chamber:
                print('#', end='')
            elif (chamber_x, chamber_y) not in rock_position:
                print('.', end='')
            else:
                print(rock_symbol, end='')
        print('\n')
    print('\n')

def write_chamber(rock_position, direction='V', rock_symbol='@'):
    global chamber_height
    with open('chamber.txt', 'a') as chamb_f:
        chamb_f.write(f'Direction: {direction}\n\n')
        for chamber_y in reversed(range(-1, chamber_height+1)):
            for chamber_x in range(-1, chamber_width+1):
                if chamber_y == -1 and (chamber_x == -1 or chamber_x == chamber_width):
                    chamb_f.write('+')
                elif chamber_y == -1:
                    chamb_f.write('-')
                elif chamber_y != -1 and (chamber_x == -1 or chamber_x == chamber_width):
                    chamb_f.write('|')
                elif (chamber_x, chamber_y) in chamber:
                    chamb_f.write('#')
                elif (chamber_x, chamber_y) not in rock_position:
                    chamb_f.write('.')
                else:
                    chamb_f.write(rock_symbol)
            chamb_f.write('\n')
        chamb_f.write('\n')


def is_touching_down(rock_position, y_bounds_down):
    for y_bound_down in y_bounds_down:
        if rock_position[y_bound_down][1] == 0 or (rock_position[y_bound_down][0], rock_position[y_bound_down][1] - 1) in chamber:
            return True
    return False

def drop_rock(rock, input_i=0, free_fall=[]):
    global chamber, chamber_height
    # print(chamber_height)
    rock_position, x_bounds, y_bounds = get_rock_start(rock)
    # write_chamber(rock_position)
    push = True
    while push or not is_touching_down(rock_position, y_bounds[1]):
        if push:
            # print('direction', input[input_i])
            rock_position = push_rock(rock_position, input[input_i], x_bounds)
            # write_chamber(rock_position, input[input_i])
            input_i += 1
            input_i %= len(input)
            push = False
        else:
            rock_position = [(x, y-1) for (x, y) in rock_position]
            # write_chamber(rock_position, input[input_i])
            push = True
    # write_chamber(rock_position, rock_symbol='#')
    chamber |= {*rock_position}
    # print('rock_bound', rock_position[y_bounds[0]][1], chamber_height)
    if rock_position[y_bounds[0]][1] + 4 > chamber_height:
        chamber_height = rock_position[y_bounds[0]][1] + 4
    return input_i

def calculate_height(height_before, begin, loop, increase, step_increase, limit):
    print(loop, increase, step_increase, limit, len(step_increase))
    left_limit = limit - begin
    print(begin, limit, left_limit)
    multiplier = left_limit // loop
    mul_increase = increase * multiplier
    leftover_steps = left_limit % loop
    if leftover_steps != 0:
        left_increase = step_increase[leftover_steps-1]
    else:
        left_increase = 0
    print(multiplier, mul_increase, leftover_steps, left_increase)
    print(height_before, mul_increase, left_increase)
    return height_before + mul_increase + left_increase - 3

# file = open('chamber.txt', 'w') 
# file.close()
rock_and_input = {}
i = 0
new_input_i = 0
loop_found = 0
second_loop_found = 0
true_loop = 0
chamber_height_start = 0
increase = 0
step_increase = []
limit = 1000000000001
# limit = 2023
while i < 10000:
    if i % 100000 == 0:
        print(i)
    if (loop_found == 0 or second_loop_found == 0) and (i%5, new_input_i) in rock_and_input:
        if loop_found == 0:
            loop_found = i
            rock_and_input = {}
        elif second_loop_found == 0:
            second_loop_found = i
            true_loop = second_loop_found - loop_found
            chamber_height_start = chamber_height
        print(i)
    all = True
    if loop_found == 0 or second_loop_found == 0:
        rock_and_input[(i%5, new_input_i)] = 1
    if increase == 0 and second_loop_found != 0 and i > second_loop_found and (i - second_loop_found) % true_loop == 0:
        increase = chamber_height - chamber_height_start
        print(calculate_height(chamber_height, i+1, true_loop, increase, step_increase, limit))
        exit()
    elif increase == 0 and second_loop_found != 0 and i != second_loop_found:
        step_increase.append(chamber_height - chamber_height_start)
    new_input_i = drop_rock(rocks[i % 5], new_input_i)
    i += 1

# write_chamber((-1, -1), 'V', '#')

result = chamber_height - 3
print("Result: {}".format(result))
