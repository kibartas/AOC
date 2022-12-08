from collections import defaultdict

input = open('input.txt', 'r').read().strip().split('\n')

rounds = [[line[0], line[2]] for line in input]

points = {'X': 1, 'Y': 2, 'Z': 3}
wins = {'X': 'C', 'Y': 'A', 'Z': 'B'}
draws = {'X': 'A', 'Y': 'B', 'Z': 'C'}

total_points = 0
for round in rounds:
    total_points += points[round[1]] 
    if wins[round[1]] == round[0]:
        total_points += 6
    elif draws[round[1]] == round[0]:
        total_points += 3
    # print(total_points)

result = total_points
print("Result: {}".format(result))
