from math import prod

input = open('input.txt', 'r').read().strip().split('\n')
touching_gear = {}

def is_touching_a_gear(x, y):
    if x+1 < len(input[0]) and not input[y][x+1].isdigit() and input[y][x+1] == '*':
        return True, (y, x+1)
    if x-1 >= 0 and not input[y][x-1].isdigit() and input[y][x-1] == '*':
        return True, (y, x-1)
    if y+1 < len(input) and not input[y+1][x].isdigit() and input[y+1][x] == '*':
        return True, (y+1, x)
    if y-1 >= 0 and not input[y-1][x].isdigit() and input[y-1][x] == '*':
        return True, (y-1, x)
    if x+1 < len(input[0]) and y+1 < len(input) and not input[y+1][x+1].isdigit() and input[y+1][x+1] == '*':
        return True, (y+1, x+1)
    if x+1 < len(input[0]) and y-1 >= 0 and not input[y-1][x+1].isdigit() and input[y-1][x+1] == '*':
        return True, (y-1, x+1)
    if x-1 >= 0 and y+1 < len(input) and not input[y+1][x-1].isdigit() and input[y+1][x-1] == '*':
        return True, (y+1, x-1)
    if x-1 >= 0 and y-1 >= 0 and not input[y-1][x-1].isdigit() and input[y-1][x-1] == '*':
        return True, (y-1, x-1)
    return False, ()
 
sum_of_nums = 0
y = 0
x = 0
while y < len(input):
    line = input[y]
    while x < len(input[0]):
        el = line[x]
        if el.isdigit():
            is_touching, gear = is_touching_a_gear(x, y)
            if is_touching:
                if gear not in touching_gear.keys():
                    touching_gear[gear] = []
                number = el
                temp_x = x
                for i in range(temp_x+1, len(input[0])):
                    if input[y][i].isdigit():
                        number += input[y][i]
                        x += 1
                    else:
                        break
                for i in range(temp_x-1, -1, -1):
                    if input[y][i].isdigit():
                        number = input[y][i] + number
                    else:
                        break
                touching_gear[gear].append(int(number))
        x += 1
    y += 1
    x = 0

sum_of_gears = sum([prod(z) for z in touching_gear.values() if len(z) > 1])

result = sum_of_gears
print("Result: {}".format(result))
