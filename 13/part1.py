input = open('input.txt', 'r').read().strip().split('\n\n')

[dots, folds] = input

dots = {tuple([int(x.split(',')[0]), int(x.split(',')[1])])
        for x in dots.split('\n')}
folds = [x.split('=') for x in folds.split('\n')]

print(dots, folds)


def fold(dots, fold):
    horizontal = True if fold[0][-1] == 'x' else False
    line = int(fold[1])
    print(fold)
    new_dots = set()
    revised_dots = dots.copy()
    if horizontal:
        for dot in dots:
            if dot[0] > line:
                new_dot = (line - (dot[0] - line), dot[1])
                if new_dot[0] < 0:
                    continue
                revised_dots.discard(dot)
                new_dots.add(new_dot)
    else:
        for dot in dots:
            if dot[1] > line:
                new_dot = (dot[0], line - (dot[1] - line))
                if new_dot[1] < 0:
                    continue
                revised_dots.discard(dot)
                new_dots.add(new_dot)
    dots = set.union(revised_dots, new_dots)
    return list(filter(lambda x: x != 'x', dots))


for i in range(0, 1):
    dots = fold(dots, folds[0])

result = len(dots)
print("Result: {}".format(result))
