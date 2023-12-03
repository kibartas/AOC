input = open('input.txt', 'r').read().strip().split('\n')
def is_touching_a_symbol(x, y):
    if x+1 < len(input[0]) and not input[y][x+1].isdigit() and input[y][x+1] != '.':
        return True
    if x-1 >= 0 and not input[y][x-1].isdigit() and input[y][x-1] != '.':
        return True
    if y+1 < len(input) and not input[y+1][x].isdigit() and input[y+1][x] != '.':
        return True
    if y-1 >= 0 and not input[y-1][x].isdigit() and input[y-1][x] != '.':
        return True
    if x+1 < len(input[0]) and y+1 < len(input) and not input[y+1][x+1].isdigit() and input[y+1][x+1] != '.':
        return True
    if x+1 < len(input[0]) and y-1 >= 0 and not input[y-1][x+1].isdigit() and input[y-1][x+1] != '.':
        return True
    if x-1 >= 0 and y+1 < len(input) and not input[y+1][x-1].isdigit() and input[y+1][x-1] != '.':
        return True
    if x-1 >= 0 and y-1 >= 0 and not input[y-1][x-1].isdigit() and input[y-1][x-1] != '.':
        return True
    return False
 
sum_of_nums = 0
y = 0
x = 0
while y < len(input):
    line = input[y]
    while x < len(input[0]):
        el = line[x]
        if el.isdigit():
            is_touching = is_touching_a_symbol(x, y)
            if is_touching:
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
                print(number)
                sum_of_nums += int(number)
        x += 1
    y += 1
    x = 0


result = sum_of_nums
print("Result: {}".format(result))
