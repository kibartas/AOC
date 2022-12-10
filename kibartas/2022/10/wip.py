import pprint

input = open('input.txt', 'r').read().strip().splitlines()

sum_signal_strength = 0

line_length = 40

screen = []
current_line = ''

cycles = 1
register_x = 1
for inst in input:
    if cycles % line_length == 1:
        screen.append(current_line)
        current_line = ''
    if abs(register_x - ((cycles % 40) - 1)) <= 1:
        current_line += '#'
    else:
        current_line += '.'
    if inst == 'noop':
        cycles += 1
    else:
        _, count = inst.split()
        cycles += 1
        if cycles % line_length == 1:
            screen.append(current_line)
            current_line = ''
        if abs(register_x - ((cycles % 40) - 1)) <= 1:
            current_line += '#'
        else:
            current_line += '.'
        cycles += 1
        register_x += int(count)
    # print(current_line, cycles, register_x)

screen.append(current_line)
pprint.pprint(screen)
with open('letters.txt', 'w') as lett:
    for line in screen:
        lett.write(line + '\n')
result = sum_signal_strength
print("Result: {}".format(result))
