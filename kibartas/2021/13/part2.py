from pprint import pprint

input = open('input.txt', 'r').read().strip().split('\n\n')

[dots, folds] = input

dots = {tuple([int(x.split(',')[0]), int(x.split(',')[1])])
        for x in dots.split('\n')}
folds = [x.split('=') for x in folds.split('\n')]


def fold(dots, fold):
    horizontal = True if fold[0][-1] == 'x' else False
    line = int(fold[1])
    print(fold)
    new_dots = set()
    print(dots)
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
    return set(filter(lambda x: x != 'x', dots))


for i in range(len(folds)):
    dots = fold(dots, folds[i])
    max_x = 0
    max_y = 0
    for dot in dots:
        if dot[0] > max_x:
            max_x = dot[0]
        if dot[1] > max_y:
            max_y = dot[1]

the_paper = open("paper.txt", "w")
for y in range(max_y+1):
    paper_line = []
    for x in range(max_x+1):
        if (x, y) in dots:
            paper_line.append('#')
        else:
            paper_line.append(' ')
    the_paper.write(str(paper_line) + '\n')


result = len(dots)
print("Result: {}".format(result))
