input = open('input.txt', 'r').read().strip().split('\n')

ranges = []
for line in input:
    pairs = line.split(',')
    temp_pair = []
    for pair in pairs:
        bounds = pair.split('-')
        temp_pair.append(bounds)
    ranges.append(temp_pair)

pair_count = 0
for pair in ranges:
    for i in range(2):
        j = (i + 1) % 2
        if (int(pair[i][0]) >= int(pair[j][0]) and int(pair[i][0]) <= int(pair[j][1])) or (int(pair[i][1]) >= int(pair[j][0]) and int(pair[i][1]) <= int(pair[j][1])):
            pair_count += 1
            print(pair)
            break



result = pair_count
print("Result: {}".format(result))
