from math import prod

input = open('input.txt', 'r').read().strip().split('\n')

colors = {'blue': 14, 'red': 12, 'green': 13}

games = []

for line in input:
    [game, sets_unf] = line.split(': ')
    # id = game.split('Game ')[1]
    sets = sets_unf.split('; ')
    fin_sets = []
    for set in sets:
        fin_set = set.split(', ')
        fin_sets.append(fin_set)
    games.append(fin_sets)

power_set_sum = 0
for i, game in enumerate(games):
    maximums = {'blue': 0, 'green': 0, 'red': 0}
    for set in game:
        for el in set:
            [count, color] = el.split(' ')
            if int(count) > maximums[color]:
                maximums[color] = int(count)
    power_set_sum += prod(maximums.values())

result = power_set_sum
print("Result: {}".format(result))
