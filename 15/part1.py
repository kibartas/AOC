input = open('input.txt', 'r').read().strip().split('\n')

matrix = []

for line in input:
    matrix.append([int(x) for x in list(line)])

memoized = {}


def move(x, y, count=0):
    if (x, y) in memoized:
        return memoized[(x, y)]
    if x+1 < len(matrix[0]) and y+1 < len(matrix):
        count += min(move(x+1, y), move(x, y+1))
    elif x+1 < len(matrix[0]):
        count += move(x+1, y)
    elif y+1 < len(matrix):
        count += move(x, y+1)
    if x != 0 or y != 0:
        count += matrix[x][y]
    memoized[(x, y)] = count
    return count


result = move(0, 0)
print(memoized[(98, 98)])
print("Result: {}".format(result))
