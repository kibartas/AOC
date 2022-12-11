import re
from collections import defaultdict

input = open('input.txt', 'r').read().strip().split('\n\n')

def get_operation_func(operation):
    if re.match(r'old \* old', operation):
        return lambda x: x**2
    elif re.match(r'old \+ old', operation):
        return lambda x: x*2
    elif re.match(r'old \* \d+', operation):
        return lambda x: x * int(operation.split('* ')[1])
    elif re.match(r'old \+ \d+', operation):
        return lambda x: x + int(operation.split('+ ')[1])
    else:
        raise Exception("HEY WHAT")
    

monkeys = []

for i, monkey in enumerate(input):
    _, items, operation, test, if_true, if_false = monkey.split('\n')
    monkeys.append([[]])

    _, parsed_items = items.split(': ')
    for item in parsed_items.split(','):
        monkeys[i][0].append(int(item))

    op_func = get_operation_func(operation.split('= ')[1])
    monkeys[i].append(op_func)

    test_number = test.split()[-1]
    monkeys[i].append(int(test_number))

    next_monkey_true = if_true.split()[-1]
    monkeys[i].append(int(next_monkey_true))

    next_monkey_false = if_false.split()[-1]
    monkeys[i].append(int(next_monkey_false))


monkey_inspection_count = defaultdict(lambda: 0)
for _ in range(20):
    for i, monkey in enumerate(monkeys):
        items = monkey[0]
        for item in items:
            new_worry = monkey[1](item)
            new_worry = new_worry // 3
            if new_worry % monkey[2] == 0:
                monkeys[monkey[3]][0].append(new_worry)
            else:
                monkeys[monkey[4]][0].append(new_worry)
            monkey_inspection_count[i] += 1
        monkeys[i][0] = []

highest_monkeys = sorted(monkey_inspection_count.values())[-2:]

result = highest_monkeys[0] * highest_monkeys[1]
print("Result: {}".format(result))
