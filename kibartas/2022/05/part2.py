from collections import defaultdict

[crates, moves] = open('input.txt', 'r').read().split('\n\n')

lines = crates.split('\n')[:-1]
print(crates)

stacks = defaultdict(lambda: [])

for i, line in enumerate(lines):
    n = 0
    stack_counter = 1
    while n < len(line):
        if line[n] == ' ':
            n += 4
        elif line[n] == '[':
            stacks[stack_counter].append(line[n+1])
            n += 4
        stack_counter += 1
        
for move in moves.split('\n'):
    [_, count, _, move_from, _, move_to] = move.split()
    count, move_from, move_to = int(count), int(move_from), int(move_to)
    crane_stack = []
    for i in range(count):
        crate = stacks[move_from].pop(0)
        crane_stack.append(crate)
    stacks[move_to] = crane_stack + stacks[move_to]



final_string = ''
for i in range(1, len(stacks)+1):
    final_string += stacks[i][0]


result = final_string
print("Result: {}".format(result))
