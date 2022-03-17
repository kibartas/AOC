input = open('input.txt', 'r').read().strip().splitlines()

positions = []

for line in input:
    positions.append(int(line.split(': ')[1]))


scores = [0, 0]
player = 0
counter = 0
global_counter = 0
number = 1
while number != 1000:
    if counter != 3:
        global_counter += 1
        positions[player] += number
        counter += 1
        number += 1
        if number == 1000:
            number = 1
        continue
    else:
        counter = 0
    positions[player] %= 10
    if positions[player] == 0:
        positions[player] = 10
    scores[player] += positions[player]
    print(global_counter)
    if scores[player] >= 1000:
        print(scores[(player+1) % 2]*global_counter)
        break
    # print(player, scores[player])
    player += 1
    player %= 2

result = scores[0] * scores[1]
print("Result: {}".format(result))
