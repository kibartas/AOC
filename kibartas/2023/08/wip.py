from math import lcm

input = open('input.txt', 'r').read().strip().split('\n')

direction, *other = input
equals_lst = other[1:]
equals = {}
start_nodes = []
for equal in equals_lst:
    start, finish = equal.split(' = ')
    equals[start] = tuple(finish.replace('(', '').replace(')', '').split(', '))
    if start.endswith('A'):
        start_nodes.append(start)

current_nodes = [[x, x] for x in start_nodes]
print(current_nodes)
counter = 0
reached_z = 0

def walk(node, direction, in_counter):
    going = direction[in_counter]
    if going == 'R':
        current_nodes[i][1] = equals[node][1]
    else:
        current_nodes[i][1] = equals[node][0]
    if current_nodes[i][1].endswith('Z'):
        return 1
    return 0

reached_zs = {}
while True:
    in_counter = counter % len(direction)
    counter += 1
    for i, (start_node, node) in enumerate(current_nodes):
        if walk(node, direction, in_counter) == 1:
            if start_node not in reached_zs:
                reached_zs[start_node] = counter
    if len(reached_zs) == len(current_nodes):
        break


print(reached_zs, len(reached_zs), len(current_nodes))

print(*list(reached_zs.values()))

result = lcm(*list(reached_zs.values()))
print("Result: {}".format(result))
