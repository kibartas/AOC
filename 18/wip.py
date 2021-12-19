from math import floor, ceil
from string import ascii_lowercase
from itertools import permutations

numbers = open('input.txt', 'r').read().strip().split('\n')

number = numbers[0]

counter = 0


def should_explode(number):
    pair_counter = 0
    for i in range(0, len(number)):
        if number[i] == '[':
            pair_counter += 1
        elif number[i] == ']':
            pair_counter -= 1
        elif pair_counter == 5:
            return True, i
    return False, 0


def explode(number, where):
    # Print the explody pair
    left_add = ''
    right_add = ''
    first_number = False
    second_number = False
    pair_bounds = [where-1]
    # print('exploded_pair', end=' ')
    for i in range(where-1, len(number)):
        # print(number[i], end='')
        if number[i] == ']':
            pair_bounds.append(i)
            break
        if first_number and number[i] == ',':
            pair_bounds.append(i)
            second_number = True
            first_number = False
        elif number[i] == '[':
            first_number = True
        elif first_number:
            left_add += number[i]
        elif second_number:
            right_add += number[i]
    # print()

    left_add = int(left_add)
    right_add = int(right_add)
    # print('left, right', left_add, right_add)

    # Add to the left
    for i in range(pair_bounds[0]-1, 0, -1):
        if ord(number[i]) >= 48 and ord(number[i]) <= 57:
            to_add_to = number[i]
            bounds = None
            for j in range(i-1, 0, -1):
                if ord(number[j]) >= 48 and ord(number[j]) <= 57:
                    to_add_to = number[j] + to_add_to
                else:
                    bounds = [j+1, i]
                    break
            # print('to_add_to_left', to_add_to)
            # print('left_bounds', bounds)
            length_before = len(to_add_to)
            to_add_to = str(int(to_add_to) + left_add)
            length_after = len(to_add_to)
            number = number[:bounds[0]] + to_add_to + number[bounds[1]+1:]
            if length_after > length_before:
                # print(length_before, length_after)
                pair_bounds[0] += length_after - length_before
                pair_bounds[1] += length_after - length_before
                pair_bounds[2] += length_after - length_before
                # print(number[pair_bounds[0]],
                #   number[pair_bounds[1]], number[pair_bounds[2]])
                # print(number)
                global counter
                counter += 1
                # if counter == 5:
                #     exit(1)
            break

    # Add to the right
    for i in range(pair_bounds[2]+1, len(number)):
        if ord(number[i]) >= 48 and ord(number[i]) <= 57:
            to_add_to = number[i]
            bounds = None
            for j in range(i+1, len(number)):
                if ord(number[j]) >= 48 and ord(number[j]) <= 57:
                    to_add_to += number[j]
                else:
                    bounds = [i, j-1]
                    break
            to_add_to = str(int(to_add_to) + right_add)
            number = number[:bounds[0]] + to_add_to + number[bounds[1]+1:]
            break

    # Replace with zero
    number = number[:pair_bounds[0]] + '0' + number[pair_bounds[2]+1:]
    return number


def should_split(number):
    for i in range(0, len(number)-1):
        # print('should_split', number[i], number[i+1])
        if ord(number[i]) >= ord('0') and ord(number[i]) <= ord('9') and ord(number[i+1]) >= ord('0') and ord(number[i+1]) <= ord('9'):
            bounds = [i]
            for j in range(i+1, len(number)):
                # print('should_split', number[j])
                if not (ord(number[j]) >= ord('0') and ord(number[j]) <= ord('9')):
                    bounds.append(j-1)
                    return True, bounds
    return False, []


def split(number, bounds):
    # print('split_bounds', bounds)
    number_to_replace = int(number[bounds[0]:bounds[1]+1])
    # print('split_number', number_to_replace)
    left_number = floor(number_to_replace / 2)
    right_number = ceil(number_to_replace / 2)
    number = number.replace(
        str(number_to_replace), f'[{left_number},{right_number}]', 1)
    return number


def check_validity(number):
    print('checking validity...')
    bracket_counter = 0
    for i in range(len(number)):
        if i+1 < len(number) and number[i] == ']' and number[i+1] != ']' and number[i+1] != ',':
            print(f'SYNTAX ERROR AT POSITION {i}: {number[i+1]}\n{number}')
            exit(1)
        if number[i] == '[':
            bracket_counter += 1
        elif number[i] == ']':
            bracket_counter -= 1
    if bracket_counter != 0:
        print('BRACKET MISMATCH')
        print(number)
        exit(1)
    print('valid')


def reduce(number):
    while True:
        # check_validity(number)
        # inp = input()
        can_explode, where = should_explode(number)
        can_split, bounds = should_split(number)
        if can_explode:
            # print('\nbefore_explosion', number)
            number = explode(number, where)
            # print('after_explosion', number)
            # check_validity(number)
        can_explode, where = should_explode(number)
        if not can_explode:
            can_split, bounds = should_split(number)
            if can_split:
                # print('\nbefore_split', number)
                number = split(number, bounds)
                # print('after_split', number)
            else:
                break

    return number


def calculate_magnitude(number):
    magnitude = 0
    last_key = None
    current_key = ascii_lowercase[0]
    key_index = 0
    keys = {}
    # print(number)
    while len(number) != 1:
        for i in range(len(number)-2):
            if number[i].isalnum() and number[i+2].isalnum():
                if number[i].isnumeric() and number[i+2].isnumeric():
                    inner_mag = int(number[i])*3 + int(number[i+2])*2
                elif number[i].isalpha() and number[i+2].isalpha():
                    inner_mag = keys[number[i]]*3 + keys[number[i+2]]*2
                elif number[i].isalpha() and number[i+2].isnumeric():
                    inner_mag = keys[number[i]]*3 + int(number[i+2])*2
                elif number[i].isnumeric() and number[i+2].isalpha():
                    inner_mag = int(number[i])*3 + keys[number[i+2]]*2
                number = number[:i-1] + current_key + number[i+4:]
                keys[current_key] = inner_mag
                key_index += 1
                last_key = current_key
                current_key = ascii_lowercase[key_index]
                break
        # print(number)

    return keys[last_key]


def try_two(numbers):
    biggest = 0
    for two in permutations(numbers, 2):
        number = f'[{two[0]},{two[1]}]'
        number = reduce(number)
        mag = calculate_magnitude(number)
        if mag > biggest:
            biggest = mag
    return biggest


for i in range(1, len(numbers)):
    print(
        f'\n\n\nROUND{i}-------------------------------------------------------------------------')
    number = f'[{number},{numbers[i]}]'
    number = reduce(number)


result_1 = calculate_magnitude(number)
print("Part 1 result: {}".format(result_1))

result_2 = try_two(numbers)
print("Part 2 result: {}".format(result_2))
