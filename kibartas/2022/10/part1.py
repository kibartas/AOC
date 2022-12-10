input = open('input.txt', 'r').read().strip().splitlines()

sum_signal_strength = 0
when_to_count = 20

cycles = 1
register_x = 1
for inst in input:
    if cycles == when_to_count:
        when_to_count += 40
        sum_signal_strength += register_x * cycles
    if inst == 'noop':
        cycles += 1
    else:
        _, count = inst.split()
        cycles += 1
        if cycles == when_to_count:
            when_to_count += 40
            sum_signal_strength += register_x * cycles
        cycles += 1
        register_x += int(count)

result = sum_signal_strength
print("Result: {}".format(result))
