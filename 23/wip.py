from time import sleep
from copy import deepcopy
input = open('sample.txt', 'r').read().strip().split('\n')

input = input[1:-1]

input[0] = input[0][1:-1]

hallway = ['_' if x == '.' else x for x in input[0]]

burrows = [[], [], [], []]

for i in range(1, 3):
    counter = 0
    for space in input[i]:
        if space != '#' and space != ' ':
            burrows[counter].append(space)
            counter += 1

print(hallway)
print(burrows)

energy = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}

hallway_over_burrow = {0: 2, 1: 4, 2: 6, 3: 8}


destinations = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
destinations_reversed = {v: k for k, v in destinations.items()}


def write_cave(file, burrows, hallway):
    for i in range(len(hallway)):
        file.write(hallway[i])
    file.write('\n')
    for i in range(len(burrows[0])):
        file.write(
            f'##{burrows[0][i]}#{burrows[1][i]}#{burrows[2][i]}#{burrows[3][i]}##')
        file.write('\n')
    file.write('\n')


def print_cave(hallway, burrows):
    for i in range(len(hallway)):
        print(hallway[i], end='')
    print()
    for i in range(len(burrows[0])):
        print(
            f'##{burrows[0][i]}#{burrows[1][i]}#{burrows[2][i]}#{burrows[3][i]}##')
    print()


print_cave(hallway, burrows)
possible_positions_in_hallway = [x for x in list(
    range(0, len(hallway))) if x not in hallway_over_burrow.values()]


def is_able_to_move_to_destination(position, burrows, amphi, hallway, in_hallway=False):
    if not in_hallway:
        position_in_hallway = hallway_over_burrow[position[0]]
    else:
        position_in_hallway = position
    destination_burrow = destinations[amphi]
    candidate_destination_position = None
    # Check if destination burrow contains his friends or is empty
    for i in range(len(burrows[destination_burrow])):
        if burrows[destination_burrow][i] == '_':
            candidate_destination_position = (destination_burrow, i)
        elif burrows[destination_burrow][i] != amphi:
            return False, None
    # Check if hallway to the burrow is empty
    if hallway_over_burrow[destination_burrow] < position_in_hallway:
        for i in range(hallway_over_burrow[destination_burrow], position_in_hallway):
            if hallway[i] != '_':
                return False, None
    else:
        for i in range(position_in_hallway+1, hallway_over_burrow[destination_burrow]):
            if hallway[i] != '_':
                return False, None
    return True, candidate_destination_position


# Tested

def is_burrow_in_order(burrow, burrow_index):
    for i in range(len(burrow)):
        if burrow[i] != destinations_reversed[burrow_index]:
            return False
    return True

# Tested


def get_movable_amphi(burrows, hallway):
    # 0 - burrows, 1 - hallway
    movable = {0: [], 1: []}
    for i in range(len(burrows)):
        # if is_burrow_in_order(burrows[i], i):
        #     continue
        for j in range(len(burrows[0])):
            if (burrows[i][j] != '_' and destinations[burrows[i][j]] != i) or (burrows[i][j] != '_' and not is_burrow_in_order(burrows[i][j+1:], i)):
                movable[0].append((i, j))
                break
            elif burrows[i][j] == '_' and is_burrow_in_order(burrows[i][j+1:], i):
                break
    for i in range(len(hallway)):
        if hallway[i] != '_' and is_able_to_move_to_destination(i, burrows, hallway[i], hallway, in_hallway=True):
            movable[1].append(i)
    return movable


def is_hallway_empty(hallway):
    for i in range(len(hallway)):
        if hallway[i] != '_':
            return False
    return True


def is_hallway_locked(hallway):
    for possible in possible_positions_in_hallway:
        if hallway[possible] == '_':
            return False
    return True


lowest_score = 15000


def check_if_done(burrows, hallway, score):
    global lowest_score
    if score >= lowest_score:
        return True
    # Check if every amphi is in it's place. If yes - we are finished
    if is_hallway_empty(hallway):
        for i, burrow in enumerate(burrows):
            if not is_burrow_in_order(burrow, i):
                return False
        if score < lowest_score:
            lowest_score = score
        return True
    return False


configurations = open('configs.txt', 'w')


def get_distance(amphi, position, candidate, from_hallway=False, to_hallway=False):
    multiplier = energy[amphi]
    if not to_hallway:
        over_burrow = hallway_over_burrow[candidate[0]]
        if from_hallway:
            distance_to_burrow = abs(position - over_burrow)
        else:
            distance_to_burrow = abs(
                hallway_over_burrow[position[0]] - over_burrow)
            distance_to_burrow += position[1] + 1
        return multiplier*(distance_to_burrow + (candidate[1] + 1))
    distance_to_burrow = abs(candidate - hallway_over_burrow[position[0]])
    return multiplier*(distance_to_burrow + position[1] + 1)


reason_count = 0
memoized_count = 0
done_count = 0
# ...D.A - impossible combination


def is_possible_to_move_to_hallway_position(from_burrow, position, hallway, amphi):
    if is_hallway_empty(hallway):
        return True
    dest = destinations[amphi]
    if dest > position:
        for i in range(position, dest):
            if hallway[i] != '_':
                his_destination = hallway_over_burrow[destinations[hallway[i]]]
                if his_destination < position:
                    return False
    else:
        for i in range(dest, position):
            if hallway[i] != '_':
                his_destination = hallway_over_burrow[destinations[hallway[i]]]
                if his_destination > position:
                    return False
    walk_from = hallway_over_burrow[from_burrow]
    for i in range(walk_from, position):
        if hallway[i] != '_':
            return False
    return True


global_counter = 0


memoized = {}


def move_into_hallway_or_destination(score, position, hallway, burrows, from_hallway=False):
    global lowest_score
    to_memoize = (hallway, burrows, position)
    if score in memoized.keys() and to_memoize in memoized[score]:
        return
    # print_cave(hallway, burrows)
    if from_hallway:
        can_move, candidate = is_able_to_move_to_destination(
            position, burrows, hallway[position], hallway, True)

        if can_move:
            new_score = score + \
                get_distance(hallway[position], position,
                             candidate, from_hallway)
            if new_score >= lowest_score:
                return
            hallway_copy = hallway.copy()
            burrows_copy = deepcopy(burrows)
            hallway_copy[position] = '_'
            burrows_copy[candidate[0]][candidate[1]] = hallway[position]
            configurations.write(str(score) + ' ' + str(new_score))
            configurations.write('\n')
            write_cave(configurations, burrows_copy, hallway_copy)
            if check_if_done(burrows_copy, hallway_copy, new_score):
                return
            if score != 0:
                if score in memoized.keys():
                    memoized[score].append(to_memoize)
                else:
                    memoized[score] = [to_memoize]
            movable_amphi = get_movable_amphi(burrows_copy, hallway_copy)
            in_burrows = movable_amphi[0]
            in_hallway = movable_amphi[1]
            for burrowed in in_burrows:
                move_into_hallway_or_destination(new_score,
                                                 burrowed, hallway_copy, burrows_copy)
            for hallwayed in in_hallway:
                move_into_hallway_or_destination(new_score,
                                                 hallwayed, hallway_copy, burrows_copy, True)
    else:
        # If burrow has an amphi above this one - can't move
        if position[1] != 0 and burrows[position[0]][position[1] - 1] != '_':
            return
        can_move, candidate = is_able_to_move_to_destination(
            position, burrows, burrows[position[0]][position[1]], hallway)
        if can_move:
            new_score = score + \
                get_distance(burrows[position[0]][position[1]],
                             position, candidate, from_hallway)
            if new_score >= lowest_score:
                return
            hallway_copy = hallway.copy()
            burrows_copy = deepcopy(burrows)
            burrows_copy[position[0]][position[1]] = '_'
            burrows_copy[candidate[0]][candidate[1]
                                       ] = burrows[position[0]][position[1]]
            configurations.write(str(score) + ' ' + str(new_score))
            configurations.write('\n')
            write_cave(configurations, burrows_copy, hallway_copy)
            if check_if_done(burrows_copy, hallway_copy, new_score):
                return
            if score != 0:
                if score in memoized.keys():
                    memoized[score].append(to_memoize)
                else:
                    memoized[score] = [to_memoize]
            movable_amphi = get_movable_amphi(burrows_copy, hallway_copy)
            in_burrows = movable_amphi[0]
            in_hallway = movable_amphi[1]
            for burrowed in in_burrows:
                move_into_hallway_or_destination(new_score,
                                                 burrowed, hallway_copy, burrows_copy)
            for hallwayed in in_hallway:
                move_into_hallway_or_destination(new_score,
                                                 hallwayed, hallway_copy, burrows_copy, True)
        else:
            for possible in possible_positions_in_hallway:
                if hallway[possible] == '_':
                    if not is_possible_to_move_to_hallway_position(position[0], possible, hallway, burrows[position[0]][position[1]]):
                        continue
                    hallway_copy = hallway.copy()
                    hallway_copy[possible] = burrows[position[0]][position[1]]
                    new_score = score + \
                        get_distance(
                            hallway_copy[possible], position, possible, from_hallway, True)
                    if score >= lowest_score:
                        continue
                    burrows_copy = deepcopy(burrows)
                    burrows_copy[position[0]][position[1]] = '_'
                    configurations.write(str(score) + ' ' + str(new_score))
                    configurations.write('\n')
                    write_cave(configurations, burrows_copy, hallway_copy)
                    if check_if_done(burrows_copy, hallway_copy, new_score):
                        return
                    if score != 0:
                        if score in memoized.keys():
                            memoized[score].append(to_memoize)
                        else:
                            memoized[score] = [to_memoize]
                    movable_amphi = get_movable_amphi(
                        burrows_copy, hallway_copy)
                    in_burrows = movable_amphi[0]
                    in_hallway = movable_amphi[1]
                    for hallwayed in in_hallway:
                        move_into_hallway_or_destination(new_score,
                                                         hallwayed, hallway_copy, burrows_copy, True)
                    for burrowed in in_burrows:
                        move_into_hallway_or_destination(new_score,
                                                         burrowed, hallway_copy, burrows_copy)


movable_amphi = get_movable_amphi(burrows, hallway)
in_burrows = movable_amphi[0]
for burrowed in in_burrows:
    print("one more")
    move_into_hallway_or_destination(0,
                                     burrowed, hallway, burrows)

result = lowest_score

print(reason_count)
print(memoized_count)
print(done_count)
print("Result: {}".format(result))
