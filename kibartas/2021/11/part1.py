input = open('input.txt', 'r').read().strip().split('\n')


# Convert to numbers
for i in range(len(input)):
    input[i] = list(input[i])
    for j in range(len(input[i])):
        input[i][j] = int(input[i][j])


def chain_reaction(input, i, j):
    if i+1 < len(input) and input[i+1][j] != 0:
        input[i+1][j] += 1
        if input[i+1][j] > 9:
            input[i+1][j] = 0
            chain_reaction(input, i+1, j)
    if i-1 >= 0 and input[i-1][j] != 0:
        input[i-1][j] += 1
        if input[i-1][j] > 9:
            input[i-1][j] = 0
            chain_reaction(input, i-1, j)
    if j+1 < len(input[i]) and input[i][j+1] != 0:
        input[i][j+1] += 1
        if input[i][j+1] > 9:
            input[i][j+1] = 0
            chain_reaction(input, i, j+1)
    if j-1 >= 0 and input[i][j-1] != 0:
        input[i][j-1] += 1
        if input[i][j-1] > 9:
            input[i][j-1] = 0
            chain_reaction(input, i, j-1)
    if i+1 < len(input) and j+1 < len(input[i]) and input[i+1][j+1] != 0:
        input[i+1][j+1] += 1
        if input[i+1][j+1] > 9:
            input[i+1][j+1] = 0
            chain_reaction(input, i+1, j+1)
    if i+1 < len(input) and j-1 >= 0 and input[i+1][j-1] != 0:
        input[i+1][j-1] += 1
        if input[i+1][j-1] > 9:
            input[i+1][j-1] = 0
            chain_reaction(input, i+1, j-1)
    if i-1 >= 0 and j+1 < len(input[i]) and input[i-1][j+1] != 0:
        input[i-1][j+1] += 1
        if input[i-1][j+1] > 9:
            input[i-1][j+1] = 0
            chain_reaction(input, i-1, j+1)
    if i-1 >= 0 and j-1 >= 0 and input[i-1][j-1] != 0:
        input[i-1][j-1] += 1
        if input[i-1][j-1] > 9:
            input[i-1][j-1] = 0
            chain_reaction(input, i-1, j-1)


flash_count = 0
for step in range(100):
    print('step ', step)
    for i in range(len(input)):
        for j in range(len(input[i])):
            input[i][j] += 1
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] > 9:
                input[i][j] = 0
                chain_reaction(input, i, j)
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == 0:
                print(i, j)
                flash_count += 1
    print(input)


# print(input)

result = flash_count
print("Result: {}".format(result))
