input = open('input.txt', 'r')

elves = []

current_elf = 0
max_elf = 0
n = 0
for line in input:
    line = line.rstrip()
    # print(line)
    if not line.isnumeric():
        elves.append(current_elf)
        if current_elf > max_elf:
            max_elf = current_elf
            n += 1
            print('Biggest elf is ' + str(n))
        current_elf = 0
    else:
        current_elf += int(line) 

elves.sort(reverse=True)
result = elves[0] + elves[1] + elves[2]
print("Result: {}".format(result))
