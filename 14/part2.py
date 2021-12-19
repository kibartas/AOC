input = open('input.txt', 'r').read().strip().split('\n\n')

template = input[0]

insertion = []

temp = input[1].split('\n')

for i in range(len(temp)):
    line = temp[i].split(' -> ')
    insertion.append((line[0], line[1]))

pairs = {}

elements = {}
# Prepare elements
for char in template:
    if char in elements.keys():
        elements[char] += 1
    else:
        elements[char] = 1

# Prepare pairs
for i in range(1, len(template)):
    key = template[i-1:i+1]
    if key in pairs.keys():
        pairs[key] += 1
    else:
        pairs[key] = 1

for i in range(0, 40):
    new_pairs = {}
    new_inserts = []
    for insert in insertion:
        key = insert[0]
        if key in pairs.keys():
            key_1 = insert[0][0] + insert[1]
            key_2 = insert[1] + insert[0][1]
            if insert[1] in elements.keys():
                elements[insert[1]] += pairs[key]
            else:
                elements[insert[1]] = pairs[key]
            if key_1 in new_pairs.keys():
                new_pairs[key_1] += pairs[key]
            else:
                new_pairs[key_1] = pairs[key]
            if key_2 in new_pairs.keys():
                new_pairs[key_2] += pairs[key]
            else:
                new_pairs[key_2] = pairs[key]
            pairs[insert[0]] -= pairs[key]
            if pairs[insert[0]] < 0:
                raise Exception("AAAAAAAAAAA")
    for key in new_pairs.keys():
        if key in pairs.keys():
            pairs[key] += new_pairs[key]
        else:
            pairs[key] = new_pairs[key]
    pairs = dict(filter(lambda x: x[1] != 0, pairs.items()))

element_map = {}
for element, frequency in elements.items():
    if element in element_map.keys():
        element_map[element] += frequency
    else:
        element_map[element] = frequency

sorted_elements = sorted(element_map.values())

most_common = sorted_elements[-1]
least_common = sorted_elements[0]

result = most_common - least_common
print("Result: {}".format(result))
