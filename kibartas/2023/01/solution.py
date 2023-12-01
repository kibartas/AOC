contents = open('input.txt').read().split('\n')

digit_strings = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def is_digit_string(line, i):
    for j, el in enumerate(digit_strings):
        internal_i = i
        not_digit = False
        for k, char in enumerate(el):
            if char != line[internal_i]:
                not_digit = True
                break
            if internal_i < len(line)-1:
                internal_i += 1
            elif k + 1 == len(el):
                break
            else:
                not_digit = True
                break
        if not not_digit:
            return str(j+1)
    return ''
         



sum = 0
for line in contents:
    first = '' 
    last = ''
    for i, char in enumerate(line):
        if char.isdigit():
            if first == '':
                first = char
            last = char
        else: 
            digit = is_digit_string(line, i)
            if digit != '':
                if first == '':
                    first = digit
                last = digit
    sum += int(first + last)

print(sum)