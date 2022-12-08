input = open('input.txt', 'r').read().strip().splitlines()


def get_scenic_score(y, x):
    target_height = input[y][x]
    scenic_score = 1
    for i in reversed(range(0, y)):
        if input[i][x] >= target_height or i == 0:
            scenic_score *= y - i
            break
    for i in range(y+1, len(input)):
        if input[i][x] >= target_height or i == len(input) - 1:
            scenic_score *= i - y
            break
    for i in reversed(range(0, x)):
        if input[y][i] >= target_height or i == 0:
            scenic_score *= x - i
            break
    for i in range(x+1, len(input[0])):
        if input[y][i] >= target_height or i == len(input[0]) - 1:
            scenic_score *= i - x
            break
    
    return scenic_score




max_scenic_score = 0
for i in range(1, len(input)-1):
    for j in range(1, len(input[0])-1):
        scenic_score = get_scenic_score(i, j)
        if scenic_score > max_scenic_score:
            max_scenic_score = scenic_score

result = max_scenic_score
print("Result: {}".format(result))
