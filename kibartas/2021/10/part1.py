input = open('input.txt', 'r').read().strip().split('\n')

print(len(input))

ends_begins = {'}': '{', ']': '[', ')': '(', '>': '<'}

corrupted = []

# [({(<(())[]>[[{[]{<()<>>
# Find first closer
# ) found, go back to find opening. ( found
# [({(<(xx)[]>[[{[]{<()<>>
# ) found. ( found.
# [({(<xxxx[]>[[{[]{<()<>>
# ] found. [ found.
# [({(<xxxxxx>[[{[]{<()<>>
# > found. < found
# [({(xxxxxxxx[[{[]{<()<>>
# ] found. [ found.
# [({(xxxxxxxx[[{xx{<()<>>
# ) found. ( found.
# [({(xxxxxxxx[[{xx{<xx<>>
# > found. < found.
# [({(xxxxxxxx[[{xx{<xxxx>
# > found. < found
# [({(xxxxxxxx[[{xx{xxxxxx

# {([(<{}[<>[]}>{[]{[(<()>
# } found. { found
# {([(<xx[<>[]}>{[]{[(<()>
# > found. < found
# {([(<xx[xx[]}>{[]{[(<()>
# ] found. [ found
# {([(<xx[xxxx}>{[]{[(<()>
# } found. [ found
# Syntax error


def check_if_corrupted(line, i, begins_symbol):
    for j in range(i-1, -1, -1):
        if line[j] == 'x':
            continue
        else:
            if line[j] != begins_symbol:
                return True, j
            else:
                return False, j


points = {')': 3, ']': 57, '}': 1197, '>': 25137}

point_sum = 0
for i, line in enumerate(input):
    is_corrupted = False
    for j in range(1, len(line)-1):
        if line[j] in ends_begins.keys():
            (is_corrupted, index) = check_if_corrupted(
                input[i], j, ends_begins[line[j]])
            if is_corrupted:
                corrupted.append(input[i])
                point_sum += points[line[j]]
                break
            else:
                input[i] = input[i][:j] + 'x' + input[i][j+1:]
                input[i] = input[i][:index] + 'x' + input[i][index+1:]


result = point_sum
print("Result: {}".format(result))
