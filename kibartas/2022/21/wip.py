import operator

ops = {'+': operator.add, '*': operator.mul, '-': operator.sub, '/': operator.ifloordiv}

input = open('input.txt', 'r').read().strip().splitlines()
monkeys = {}
for el in input:
    name, *rest = el.split()
    name = name[:-1]
    if len(rest) == 1:
        monkeys[name] = rest[0]
    else:
        monkeys[name] = rest
    # print(name, rest)

monkeys['humn'] = '?'
print(monkeys)

def get_result(element):
    if isinstance(monkeys[element], str):
        return monkeys[element]
    else:
        monkey = monkeys[element]
        string =  '(' + get_result(monkey[0]) + monkey[1] +  get_result(monkey[2]) + ')'
        if '?' not in string:
            return str(eval(string))
        return string
# print(monkeys['drzm']())

first = get_result(monkeys['root'][0])
second = get_result(monkeys['root'][2])
known = None
unknown = None
if '?' in first:
    if '?' in second:
        print("WTF")
        exit()
    known = eval(second)
    unknown = first
else:
    known = eval(first)
    unknown = second
print(known, unknown)
found_candidate = None
i = 3952288600000
higher_bound = 3952288700000
candidate_zero = unknown.replace('?', str(i))
more = eval(candidate_zero) > known
while i < higher_bound:
    if i % 100000 == 0:
        print(i)
    candidate = unknown.replace('?', str(i))
    candidate_eval = eval(candidate)
    if candidate_eval == known:
        found_candidate = i
        break
    elif candidate_eval > known and not more:
        print("THATS IT", i)
        break
    elif candidate_eval < known and more:
        print("THATS IT", i)
        break
    i += 1

# assert get_result(monkeys['root'][0]) == get_result(monkeys['root'][2])
result = found_candidate
print("Result: {}".format(result))
