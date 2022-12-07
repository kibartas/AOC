input = open('input.txt', 'r').read().strip().split('\n')

def get_char_priority(char):
    char = ord(char)
    return char - 96 if char > 96 else char - 38

sum = 0
for i in range(0, len(input), 3):
    group = input[i:i+3]
    for char in group[0]:
        if group[1].find(char) != -1 and group[2].find(char) != -1:
            sum += get_char_priority(char)
            break
                 

result = sum
print("Result: {}".format(result))
