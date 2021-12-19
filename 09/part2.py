input = [item for item in open(
    'input.txt', 'r').read().strip().split('\n')]

used_input = []


def go_all_four(fromi, fromj, input, line):
    size = 0
    # Horizontal +
    size = 0
    for k in range(fromj+1, len(line)):
        if int(input[fromi][k]) < 9 and int(input[fromi][k]) > int(input[fromi][k-1]) and not (fromi, k) in used_input:
            used_input.append((fromi, k))
            size += 1 + go_all_four(fromi, k, input, line)
        else:
            break
    # Horizontal -
    for k in range(fromj-1, -1, -1):
        if int(input[fromi][k]) < 9 and int(input[fromi][k]) > int(input[fromi][k+1]) and not (fromi, k) in used_input:
            used_input.append((fromi, k))
            size += 1 + go_all_four(fromi, k, input, line)
        else:
            break

    # Vertical +
    for k in range(fromi+1, len(input)):
        if int(input[k][fromj]) < 9 and int(input[k][fromj]) > int(input[k-1][fromj]) and not (k, fromj) in used_input:
            used_input.append((k, fromj))
            size += 1 + go_all_four(k, fromj, input, line)
        else:
            break

    # Vertical -
    for k in range(fromi-1, -1, -1):
        if int(input[k][fromj]) < 9 and int(input[k][fromj]) > int(input[k+1][fromj]) and not (k, fromj) in used_input:
            used_input.append((k, fromj))
            size += 1 + go_all_four(k, fromj, input, line)
        else:
            break

    return size


sizes = []
for i, line in enumerate(input):
    for j, num in enumerate(line):
        num = int(num)
        if (i, j) in used_input:
            continue
        if i+1 < len(input) and not num < int(input[i+1][j]):
            continue
        if i-1 >= 0 and not num < int(input[i-1][j]):
            continue
        if j+1 < len(line) and not num < int(line[j+1]):
            continue
        if j-1 >= 0 and not num < int(line[j-1]):
            continue
        size = 1

        used_input.append((i, j))

        size += go_all_four(i, j, input, line)

        sizes.append(size)

sizes.sort(reverse=True)
result = sizes[0] * sizes[1] * sizes[2]
print("Result: {}".format(result))
