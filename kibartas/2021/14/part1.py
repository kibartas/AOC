input = open('input.txt', 'r').read().strip().split('\n\n')

template = input[0]

insertion = []

temp = input[1].split('\n')

for i in range(len(temp)):
    line = temp[i].split(' -> ')
    insertion.append((line[0], line[1]))

for i in range(0, 10):
    new_inserts = []
    for insert in insertion:
        if insert[0] in template:
            new_inserts.append(insert)
    for insert in new_inserts:
        while (True):
            new_template = template.replace(
                insert[0], insert[0][0] + chr(ord(insert[1]) + 32) + insert[0][1])
            if template == new_template:
                break
            template = new_template
    template_list = list(template)
    for i in range(len(template_list)):
        if template_list[i].islower():
            template_list[i] = template_list[i].upper()
    template = ''.join(template_list)

element_map = {}
for element in template:
    if element in element_map.keys():
        element_map[element] += 1
    else:
        element_map[element] = 1

sorted_elements = sorted(element_map.values())

most_common = sorted_elements[-1]
least_common = sorted_elements[0]

result = most_common - least_common
print("Result: {}".format(result))

# NBCCNBBBCBHCB
# NbBbCnCcNbBnBnBbChBhHbChB
# NBBBCNCCNBBNBNBBCHBHHBCHB
