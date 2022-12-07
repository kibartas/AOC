input = open('input.txt', 'r').read().strip().split('\n')

rounds = [[line[0], line[2]] for line in input]

points = {'X': 1, 'Y': 2, 'Z': 3}
wins = {'X': 'C', 'Y': 'A', 'Z': 'B'}
draws = {'X': 'A', 'Y': 'B', 'Z': 'C'}
losses = {'X': 'B', 'Y': 'C', 'Z': 'A'}
reverse_wins = {v: k for k, v in wins.items()}
reverse_draws = {v: k for k, v in draws.items()}
reverse_losses = {v: k for k, v in losses.items()}


total_points = 0
for round in rounds:
    if round[1] == 'X':
        total_points += points[reverse_losses[round[0]]]
        total_points += 0
    elif round[1] == 'Y':
        total_points += points[reverse_draws[round[0]]]
        total_points += 3
    elif round[1] == 'Z':
        total_points += points[reverse_wins[round[0]]]
        total_points += 6
    
    # print(total_points)

result = total_points
print("Result: {}".format(result))
