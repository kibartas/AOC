input = open('input.txt', 'r').read().strip().split('\n')

time, distance = int(''.join(input[0].split(':')[1].split())), int(''.join(input[1].split(':')[1].split()))
print(time, distance)

winning_times_prod = 1
winning_times = 0
for j in range(1, time):
    traveled = (time - j) * j
    if traveled > distance:
        winning_times += 1
winning_times_prod *= winning_times


result = winning_times_prod
print("Result: {}".format(result))
