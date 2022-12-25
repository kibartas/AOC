import re
from collections import defaultdict

input = open('input.txt', 'r').read().strip().split('\n\n')

def get_operation_func(operation):
    if re.match(r'old \* old', operation):
        return lambda x: {divisor: (modulus ** 2) % divisor for divisor, modulus in x.items()}
    elif re.match(r'old \+ old', operation):
        return lambda x: {divisor: (modulus * 2) % divisor for divisor, modulus in x.items()}
    elif re.match(r'old \* \d+', operation):
        return lambda x: {divisor: (modulus * int(operation.split('* ')[1])) % divisor for divisor, modulus in x.items()}
    elif re.match(r'old \+ \d+', operation):
        return lambda x: {divisor: (modulus + int(operation.split('+ ')[1])) % divisor for divisor, modulus in x.items()}
    else:
        raise Exception("HEY WHAT")


all_divisors = []

def get_moduli(number):
    moduli = {}
    for divisor in all_divisors:
        moduli[divisor] = (number % divisor)
    return moduli
    

for i, monkey in enumerate(input):
    _, _, _, test, _, _ = monkey.split('\n')
    test_number = test.split()[-1]
    all_divisors.append(int(test_number))

monkeys = []

for i, monkey in enumerate(input):
    _, items, operation, test, if_true, if_false = monkey.split('\n')
    monkeys.append([[]])

    _, parsed_items = items.split(': ')
    for item in parsed_items.split(','):
        moduli = get_moduli(int(item))
        monkeys[i][0].append(moduli)

    op_func = get_operation_func(operation.split('= ')[1])
    monkeys[i].append(op_func)

    test_number = test.split()[-1]
    monkeys[i].append(int(test_number))

    next_monkey_true = if_true.split()[-1]
    monkeys[i].append(int(next_monkey_true))

    next_monkey_false = if_false.split()[-1]
    monkeys[i].append(int(next_monkey_false))


monkey_inspection_count = defaultdict(lambda: 0)
for round in range(10000):
    for i, monkey in enumerate(monkeys):
        items = monkey[0]
        for item in items:
            new_worry = monkey[1](item)
            if new_worry[monkey[2]] == 0:
                monkeys[monkey[3]][0].append(new_worry)
            else:
                monkeys[monkey[4]][0].append(new_worry)
            monkey_inspection_count[i] += 1
        monkeys[i][0] = []

highest_monkeys = sorted(monkey_inspection_count.values())[-2:]

result = highest_monkeys[0] * highest_monkeys[1]
print("Result: {}".format(result))
