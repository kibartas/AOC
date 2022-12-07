input = open('input.txt', 'r')

elves = {}

current_elf = 0
max_elf = 0
n = 0
for line in input:
    line = line.rstrip()
    # print(line)
    if not line.isnumeric():
        if current_elf > max_elf:
            max_elf = current_elf
            n += 1
            print('Biggest elf is ' + str(n))
        current_elf = 0
    else:
        current_elf += int(line) 

result = max_elf
print("Result: {}".format(result))
