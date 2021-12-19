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


def mark_complete_chunks(input, i):
    points = {')': 3, ']': 57, '}': 1197, '>': 25137}
    is_corrupted = False
    for j in range(1, len(input[i])):
        if input[i][j] in ends_begins.keys():
            (is_corrupted, index) = check_if_corrupted(
                input[i], j, ends_begins[input[i][j]])
            if is_corrupted:
                corrupted.append(input[i])
                return points[input[i][j]]
            else:
                input[i] = input[i][:j] + 'x' + input[i][j+1:]
                input[i] = input[i][:index] + 'x' + input[i][index+1:]
    return 0


corrupted_points = 0

# Corrupted
for i in range(len(input)):
    corrupted_points += mark_complete_chunks(input, i)


# Only leave incomplete ones

incomplete = filter(lambda x: x not in corrupted, input)

incomplete_pointing_system = {'(': 1, '[': 2, '{': 3, '<': 4}
incomplete_point_list = []

for line in incomplete:
    incomplete_points = 0
    for i in range(len(line)-1, -1, -1):
        if line[i] == 'x':
            continue
        else:
            incomplete_points *= 5
            incomplete_points += incomplete_pointing_system[line[i]]
    incomplete_point_list.append(incomplete_points)

result = sorted(incomplete_point_list)[len(incomplete_point_list)/2]

# [({(<(())[]>[[{[]{<()<>>
# [({(xxxxxxxx[[{xx{xxxxxx
# found openings [({([[{{

print("Result: {}".format(result))
