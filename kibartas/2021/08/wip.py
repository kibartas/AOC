input = map(lambda x: map(lambda y: y.split(' '), x.split(' | ')), open(
    'input.txt', 'r').read().strip().split('\n'))

digits = {
    1: ("c", "f"),
    7: ("a", "c", "f"),
    4: ("b", "c", "d", "f"),
    8: ("a", "b", "c", "d", "e", "f", "g"),
}
# Obvious which one is 1, 7 or 4
# If 5 letter has both 1s letters - it's 3
# If 5 letter matches 3 four's letters - it's 5
# The only 5 letter left is 2
# If 6 letter does not have all of 1s letters it is 6
# If 6 letter matches all of 4 letters it is 9
# The only one 6 letter left is 0

nonUniqueDigits = {
    2: ("a", "c", "d", "e", "g"),
    3: ("a", "c", "d", "f", "g"),
    5: ("a", "b", "d", "f", "g"),
    0: ("a", "b", "c", "e", "f", "g"),
    6: ("a", "b", "d", "e", "f", "g"),
    9: ("a", "b", "c", "d", "f", "g"),
}


# Obvious which one is 1, 7 or 4
# If 5 letter has both 1s letters - it's 3
# If 5 letter matches 3 four's letters - it's 5
# The only 5 letter left is 2
# If 6 letter does not one of 1s letters it is 6
# If 6 letter matches all of 4 letters it is 9
# The only one 6 letter left is 0
def solve(wires):
    solutions = {}
    solutions[1] = wires[0]
    solutions[7] = wires[1]
    solutions[4] = wires[2]
    solutions[8] = wires[9]

    for i in range(3, 6):
        match_count = 0
        for char in solutions[1]:
            if char in wires[i]:
                match_count += 1
        if match_count == 2:
            solutions[3] = wires[i]
            wires[i] = 'x'
            break
    # Found 3
    for i in range(3, 6):
        match_count = 0
        for char in solutions[4]:
            if char in wires[i]:
                match_count += 1
        if match_count == 3:
            solutions[5] = wires[i]
            wires[i] = 'x'
            break
    # Found 5
    for i in range(3, 6):
        if wires[i] != 'x':
            solutions[2] = wires[i]
            wires[i] = 'x'
            break
    # Found 2
    for i in range(6, 9):
        match_count = 0
        for char in solutions[1]:
            if char in wires[i]:
                match_count += 1
        if match_count == 1:
            solutions[6] = wires[i]
            wires[i] = 'x'
            break
        else:
            if i == 8:
                print('wtf')
    # Found 6
    for i in range(6, 9):
        match_count = 0
        for char in solutions[4]:
            if char in wires[i]:
                match_count += 1
        if match_count == 4:
            solutions[9] = wires[i]
            wires[i] = 'x'
            break
    # Found 9
    for i in range(6, 9):
        if wires[i] != 'x':
            solutions[0] = wires[i]
            wires[i] = 'x'
            break
    # Found 0

    return solutions


final_sum = 0
for line in input:
    wires = []
    line[0] = sorted(line[0], key=lambda x: len(x))
    for wirings in line[0]:
        wires.append(''.join(sorted(wirings)))

    final_number = ''
    deciphered_wires = solve(wires)
    for whats_on_screen in line[1]:
        whats_on_screen = ''.join(sorted(whats_on_screen))
        for k, v in deciphered_wires.items():
            if v == whats_on_screen:
                final_number += str(k)
                break
    final_sum += int(final_number)


# print(input)
result = final_sum
print("Result: {}".format(result))
