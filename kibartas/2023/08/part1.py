input = open('input.txt', 'r').read().strip().split('\n')

direction, *other = input
equals_lst = other[1:]
equals = {}
for equal in equals_lst:
    start, finish = equal.split(' = ')
    equals[start] = tuple(finish.replace('(', '').replace(')', '').split(', '))

current_node = 'AAA'
counter = 0
while True:
    in_counter = counter % len(direction)
    counter += 1
    going = direction[in_counter]
    if going == 'R':
        current_node = equals[current_node][1]
    else:
        current_node = equals[current_node][0]
    
    if current_node == 'ZZZ':
        break

result = counter
print("Result: {}".format(result))
