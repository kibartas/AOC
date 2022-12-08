import sys
from itertools import product

input = open('input.txt', 'r').read().strip().splitlines()
point_goal = 21

positions = []

sys.setrecursionlimit(15000)

for line in input:
    positions.append(int(line.split(': ')[1]))

wins = [0, 0]
# Play until 10
# 10
# 7
# Roll 1 u_count = 1
# universes = { (1, 1, 1): 1, (2, 2, 1): 1, (3, 3, 1): 1 }
# Roll 2 u_count = 3
# universes = { (2, 3, 1): 3, (2, 2, 1): 3, (3, 3, 1): 3 }
# Roll 3 u_count = 9
# universes = { (1, 1, 1): 3, (2, 2, 1): 3, (3, 3, 1): 3, (8, 8, 2): 3, (9, 9, 2): 3, (10, 10, 2): 3 }


# Play until 21
# 10
# 7
# Roll 1 u_count = 1
# universes = { (1, 1, 1): 1, (2, 2, 1): 1, (3, 3, 1): 1 }
# Roll 2 u_count = 3
# universes = { (1, 1, 1): 3, (2, 2, 1): 3, (3, 3, 1): 3, (8, 8, 2): 3, (9, 9, 2): 3, (10, 10, 2): 3 }
# Roll 3 u_count = 9
# universes = { (1, 1, 1): 3, (2, 2, 1): 3, (3, 3, 1): 3, (8, 8, 2): 3, (9, 9, 2): 3, (10, 10, 2): 3 }


def roll(position, dice_roll):
    if position > 10:
        raise Exception("WHAT IN POSTARNATION")
    result = position + dice_roll
    if result % 10 != 0:
        result %= 10
    else:
        result = 10
    if result > 10:
        raise Exception("WHAT IN TARNATION")
    return result


wins = [0, 0]


def eat(universes, player):
    other_player = (player+1) % 2
    new_universes = {x: v for x,
                     v in universes[player].items() if x[1] < point_goal}
    # print("MEAN", floor(mean(new_universes.values())))
    # if sum(wins) > 444356092776315 + 341960390180808:
    #     raise Exception(sum(wins), 444356092776315 + 341960390180808)
    universes_to_remove = sum(x[0] * x[1] for x in universes[player].values(
    )) - sum(x[0] * x[1] for x in new_universes.values())
    wins[player] += universes_to_remove
    if universes_to_remove == 0:
        return universes
    print("THESE ARE THE UNIVERSES", universes)
    print("GONNA REMOVE", universes_to_remove)
    count_of_elements_in_other = sum(
        [count[1] for count in universes[other_player].values()])
    # print(wins)
    from_each = universes_to_remove // count_of_elements_in_other
    print("BUT ONLY THIS MUCH FROM EACH", from_each)
    print(f"BECAUSE THERE ARE {count_of_elements_in_other} ELEMENTS")
    print("FROM HERE", universes[other_player])
    for universe in universes[other_player]:
        universes[other_player][universe][0] -= from_each
    print("AFTER REMOVAL", universes[other_player])
    universes[player] = new_universes
    return universes


def dirac(universes, available_dice_rolls):
    player = 0
    other_player = 1
    while True:
        # print("ROLL", r)
        new_universes = {}
        for dice_roll in available_dice_rolls:
            for universe, count in universes[player].items():
                new_position = roll(universe[0], dice_roll)
                new_score = universe[1] + new_position
                if (new_position, new_score) in new_universes.keys():
                    new_universes[(new_position, new_score)][1] += count[1]
                else:
                    new_universes[(new_position, new_score)] = [
                        count[0], count[1]]
        universes[player] = new_universes
        # print("SUMS", sum(x[0] * x[1] for x in universes[player].values()),
        #       sum(x[0] * x[1] for x in universes[other_player].values()))
        for other_universe in universes[other_player].keys():
            universes[other_player][other_universe][0] *= len(
                available_dice_rolls)
        universes[player] = new_universes
        # print("D", universes)
        print("SUMS", sum(x[0] * x[1] for x in universes[player].values()),
              sum(x[0] * x[1] for x in universes[other_player].values()))
        universes = eat(universes, player)
        # if sum(x[0] * x[1] for x in universes[player].values()) > 444356092776315 + 341960390180808:
        #     print(universes)
        #     raise Exception("HEY")
        if len(universes[player]) == 0:
            return
        player = other_player
        other_player = (other_player + 1) % 2


permute = product('123', repeat=3)

available_points = []
for perm in permute:
    print(perm)
    s = 0
    for digit in perm:
        s += int(digit)
    available_points.append(s)
print(available_points)
# Roll 0
# universes = { 0: {(4, 0): 1 }, 1: { (8, 0): 1} }
# Roll 1
# {1, 2, 3} - {1, 2, 3} - {1, 2, 3}
# universes = { 0: {(7, 7): 1, (8, 8): 1, (9, 9): 1, (10, 10): 1, (1, 1): 1, (2, 2): 1, (3, 3): , 1: { (8, 0): 1 }}
assert roll(0, 100) == 10
assert roll(5, 15) == 10
assert roll(5, 10) == 5
assert roll(1, 9) == 10
dirac({0: {(positions[0], 0): [1, 1]}, 1: {
      (positions[1], 0): [1, 1]}}, available_points)
print(wins)
