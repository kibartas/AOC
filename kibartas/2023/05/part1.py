from copy import deepcopy

input = [x for x in open('input.txt', 'r').read().strip().split('\n')]

chains = [[int(x)] for x in input[0].split('seeds: ')[1].split()]
maps = {}

i = 2
while i < len(input):
    line = input[i]
    split_at_dash = line.split('-')
    to = split_at_dash[2].split(' ')[0]
    fr = split_at_dash[0]
    maps[(fr, to)] = []
    j = i + 1
    while True:
        if j >= len(input) or input[j] == '':
            break
        maps[(fr, to)].append([int(x) for x in input[j].split()])
        j += 1
    i = j + 1

def chain(groups, index):
    new_chains = deepcopy(chains)
    for i, chain in enumerate(chains):
        current_num = chain[index]
        for group in groups:
            dest, src, range = group
            if current_num >= src and current_num <= src + range:
                new_chains[i].append(dest + (current_num - src))
        if len(new_chains[i]) == index+1:
            new_chains[i].append(new_chains[i][index])
    return new_chains


i = 0
for i, (_, groups) in enumerate(maps.items()):
    chains = chain(groups, i)

lowest_loc = 0
for chain_ in chains:
    if lowest_loc == 0:
        lowest_loc = chain_[-1]
    if chain_[-1] < lowest_loc:
        lowest_loc = chain_[-1]

print(chains)
result = lowest_loc
print("Result: {}".format(result))
