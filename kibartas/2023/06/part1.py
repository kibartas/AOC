input = open('input.txt', 'r').read().strip().split('\n')

times, distances = [int(x) for x in input[0].split(':')[1].split()], [int(x) for x in input[1].split(':')[1].split()]

winning_times_prod = 1
for i, time in enumerate(times):
    winning_times = 0
    for j in range(1, time):
        traveled = (time - j) * j
        if traveled > distances[i]:
            winning_times += 1
    winning_times_prod *= winning_times


result = winning_times_prod
print("Result: {}".format(result))
