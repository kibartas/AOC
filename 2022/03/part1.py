input = open('input.txt', 'r').read().strip().split('\n')

def get_char_priority(char):
    char = ord(char)
    return char - 96 if char > 96 else char - 38

in_half = [[line[:len(line)//2], line[len(line)//2:]] for line in input]

sum = 0
for a, b in in_half:
    for char in a:
        if b.find(char) != -1:
            sum += get_char_priority(char)
            break
                 

result = sum
print("Result: {}".format(result))
