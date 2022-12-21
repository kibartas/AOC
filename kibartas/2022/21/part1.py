import operator

ops = {'+': operator.add, '*': operator.mul, '-': operator.sub, '/': operator.ifloordiv}

input = open('input.txt', 'r').read().strip().splitlines()
monkeys = {}
for el in input:
    name, *rest = el.split()
    name = name[:-1]
    if len(rest) == 1:
        monkeys[name] = int(rest[0])
    else:
        monkeys[name] = rest
    # print(name, rest)

print(monkeys)

def get_result(element='root'):
    if isinstance(monkeys[element], int):
        return monkeys[element]
    else:
        monkey = monkeys[element]
        return ops[monkey[1]](get_result(monkey[0]), get_result(monkey[2]))
# print(monkeys['drzm']())


result = get_result()
print("Result: {}".format(result))
