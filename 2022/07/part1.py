input = open('input.txt', 'r').read().strip().splitlines()

file_tree = {}
current_dir = None

def add_size_to_parents(file_tree, current_dir, size):
    if current_dir is None:
        return
    parent_dir = file_tree[current_dir][1]
    if parent_dir is None:
        return
    file_tree[parent_dir][0] += size

    add_size_to_parents(file_tree, parent_dir, size)

current_dir_counter = 0
for i, line in enumerate(input):
    if line.startswith('$ cd'):
        if line.split()[2] == '..':
            current_dir = file_tree[current_dir][1]
        else:
            next_dir = current_dir_counter
            file_tree[next_dir] = [0, current_dir]
            current_dir = next_dir
            current_dir_counter += 1
    elif line.startswith('$ ls') or line.startswith('dir'):
        continue
    else:
        file_size = int(line.split()[0])
        file_tree[current_dir][0] += file_size
        if i+1 == len(input) or input[i+1].startswith('$'):
            current_dirs = []
            add_size_to_parents(file_tree, current_dir, file_tree[current_dir][0])

final_sum = 0
for v in file_tree.values():
    if v[0] <= 100000:
        final_sum += v[0]


result = final_sum
print("Result: {}".format(result))
