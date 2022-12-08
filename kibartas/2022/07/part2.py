input = open('input.txt', 'r').read().strip().splitlines()

file_tree = {}

def add_size_to_parents(cur_dir, size):
    parent_dir = '/'.join(cur_dir.split('/')[:-2]) + '/'
    file_tree[parent_dir] += size
    if parent_dir == '/':
        return

    add_size_to_parents(parent_dir, size)

current_dir = None
for i, line in enumerate(input):
    if line.startswith('$ cd'):
        _, _, dir = line.split()
        if dir == '..':
            current_dir = '/'.join(current_dir.split('/')[:-2]) + '/'
        else:
            if current_dir is None:
                path = dir
            else:
                path = current_dir + dir + '/'
            file_tree[path] = 0
            current_dir = path
    elif line.startswith('$ ls'):
        continue
    else:
        if not line.startswith('dir'):
            file_size = int(line.split()[0])
            file_tree[current_dir] += file_size
        if current_dir != '/' and file_tree[current_dir] != 0 and (i+1 == len(input) or input[i+1].startswith('$')):
            add_size_to_parents(current_dir, file_tree[current_dir])

root_size = file_tree['/']
print(file_tree)
candidate_dir_size = float('inf')
for v in file_tree.values():
    if root_size - v < 40000000 and v < candidate_dir_size:
        candidate_dir_size = v


result = candidate_dir_size
print("Result: {}".format(result))
