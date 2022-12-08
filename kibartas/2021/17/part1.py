input = map(lambda x: x.split('=')[1].split('..'), open(
    'input.txt', 'r').read().strip().split(': ')[1].split(', '))

input[0][0] = int(input[0][0])
input[0][1] = int(input[0][1])
input[1][0] = int(input[1][0])
input[1][1] = int(input[1][1])

file = open('map.txt', 'w')

y_lowest_target_area = min(input[1][0], input[1][1])
y_highest_target_area = max(input[1][0], input[1][1])

x_lowest_target_area = min(input[0][0], input[0][1])
x_highest_target_area = max(input[0][0], input[0][1])


# S = (a_1 + a_n)*n / 2
# (a_1 + a_n) * n / 2 = (20, 30)
# (1 + a_n) * n / 2 = (20, 30)
# (1 + 0) * 2 / 2 = (20, 30)
# (2 + 1) * 2 / 2 = (20, 30)
# (2 + 0) * 3 / 2 = (20, 30)

x_candidates = []
for a_1 in range(1, 100000, 1):
    if a_1 > x_highest_target_area:
        break
    counter = 1
    for a_n in range(a_1, 0, -1):
        sum = (a_1 + a_n)*counter / 2
        if sum >= x_lowest_target_area and sum <= x_highest_target_area:
            if counter == a_1:
                x_candidates.append((a_1, '>={}'.format(a_1)))
            else:
                x_candidates.append((a_1, counter))
        counter += 1

print(x_candidates)

y_candidates = []
for a_1 in range(1, 1000, 1):
    counter = 1
    a_n = a_1
    highest = 0
    while True:
        if sum > highest:
            highest = sum
        sum = (a_1 + a_n)*counter / 2
        if sum >= y_lowest_target_area and sum <= y_highest_target_area:
            y_candidates.append((a_1, counter, highest))
        counter += 1
        if sum < y_lowest_target_area:
            break
        a_n -= 1


print(y_candidates)
result = 0
print("Result: {}".format(result))
