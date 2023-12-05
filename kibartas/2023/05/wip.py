input = [x for x in open('input.txt', 'r').read().strip().split('\n')]

seeds_only = input[0].split('seeds: ')[1].split()
chains = []
i = 0
while i < len(seeds_only):
    chains.append((int(seeds_only[i]), int(seeds_only[i]) + int(seeds_only[i+1])))
    i += 2
chains = chains
print(chains)
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

def inner_chain(bounds, groups):
    new_chains = []
    print(bounds)
    first, second = bounds
    done = False
    for group in groups:
        dest, src, range = group
        to_add = dest - src
        if first >= src and first < src + range:
            bound = src + range
            if second < bound:
                new_chains.append((first + to_add, second+to_add))
                done = True
                break
            else:
                new_chains.append((first + to_add, bound - 1 + to_add))
                first = bound
        elif second >= src and second < src + range:
            bound = src
            new_chains.append((bound + to_add, second+to_add))
            second = bound - 1
        elif first < src and second > src:
            new_chains.append((src + to_add, src + range + to_add))
            done = True
            break
    if not done:
        new_chains.append((first, second))
    return new_chains

def chain(groups):
    new_chains = []
    for bounds in chains:
        print('hello?', bounds)
        new_chains += inner_chain(bounds, groups)
    return new_chains


for name, groups in maps.items():
    # print(name)
    chains = chain(groups)
    # print(chains)

lowest_loc = None 
for chain_ in chains:
    if lowest_loc is None:
        lowest_loc = chain_[0]
    if chain_[0] > chain_[1]:
        raise Exception("AAAAAAAAAA")
    if chain_[0] < lowest_loc:
        lowest_loc = chain_[0]

# print(chains, len(chains))
result = lowest_loc
print("Result: {}".format(result))
