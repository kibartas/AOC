input = open('input.txt', 'r').read().strip().split('\n')


games = []
for line in input:
    (win, game) = line.split(': ')[1].split(' | ')
    games.append(([x for x in win.split(' ') if x != ''], [x for x in game.split(' ') if x != '']))

scratchcard_count = len(games)

def scratch(game, i):
    current_game = 0
    scratchcard_count = 0
    for el in game[1]:
        if el in game[0]:
            current_game += 1
    scratchcard_count += current_game
    for j in range(i+1, i+1+current_game):
        scratchcard_count += scratch(games[j], j)
    return scratchcard_count
for i, game in enumerate(games):
    wins = scratch(game, i)
    scratchcard_count += wins


result = scratchcard_count 
print("Result: {}".format(result))
