input = open('input.txt', 'r').read().strip().split('\n')


games = []
for line in input:
    (win, game) = line.split(': ')[1].split(' | ')
    games.append(([x for x in win.split(' ') if x != ''], [x for x in game.split(' ') if x != '']))

point_sum = 0
for game in games:
    current_game = 0
    for el in game[1]:
        if el in game[0]:
            if current_game == 0:
                current_game += 1
            else:
                current_game *= 2
    point_sum += current_game    


result = point_sum
print("Result: {}".format(result))
