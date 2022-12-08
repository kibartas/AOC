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
    if (int(pair[0][0]) >= int(pair[1][0]) and int(pair[0][1]) <= int(pair[1][1])) or (int(pair[1][0]) >= int(pair[0][0]) and int(pair[1][1]) <= int(pair[0][1])):
        pair_count += 1



result = pair_count
print("Result: {}".format(result))
