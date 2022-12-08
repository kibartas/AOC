input = open('input.txt', 'r').read().strip().split('\n')

sum = 0
for i, line in enumerate(input):
    for j, num in enumerate(line):
        if i+1 < len(input) and not num < input[i+1][j]:
            continue
        if i-1 >= 0 and not num < input[i-1][j]:
            continue
        if j+1 < len(line) and not num < line[j+1]:
            continue
        if j-1 >= 0 and not num < line[j-1]:
            continue
        sum += int(num) + 1


result = sum
print("Result: {}".format(result))
