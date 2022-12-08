input = open('input.txt', 'r').read().strip().splitlines()


def is_visible(y, x):
    target_height = input[y][x]
    for i in reversed(range(0, y)):
        if input[i][x] >= target_height:
            break
        elif i == 0:
            return 1
    for i in range(y+1, len(input)):
        if input[i][x] >= target_height:
            break
        elif i == len(input) - 1:
            return 1
    for i in reversed(range(0, x)):
        if input[y][i] >= target_height:
            break
        elif i == 0:
            return 1
    for i in range(x+1, len(input[0])):
        if input[y][i] >= target_height:
            break
        elif i == len(input[0])-1:
            return 1
    
    return 0




visible_counter = 0
for i in range(1, len(input)-1):
    for j in range(1, len(input[0])-1):
        visible_counter += is_visible(i, j)

result = visible_counter + (len(input[0]) + len(input)) * 2 - 4 # remove corners
print("Result: {}".format(result))
