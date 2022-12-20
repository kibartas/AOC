input = open('input.txt', 'r').read().strip().splitlines()
input = [(int(x), i) for i, x in enumerate(input)]
zero_pair = None
for i, pair in enumerate(input):
    if pair[0] == 0:
        zero_pair = pair
        break

input_copy = [*input]
file = open('lines.txt', 'w')

i = 0
while i < len(input_copy):
    element = input_copy[i]
    real_i = input.index(element)
    move_by = element[0]
    wanted_pos = (real_i + move_by)%(len(input_copy) - 1)
    # print(wanted_pos, real_i, move_by, len(input))
    if move_by != 0:
        if wanted_pos == 0:
            input = input[:real_i] + input[real_i+1:len(input_copy)] + [element]
        elif (real_i + move_by) % len(input) == len(input_copy)-1:
            input = [element] + input[:real_i] + input[real_i+1:len(input_copy)]
        elif wanted_pos > real_i:
            input = input[:real_i] + input[real_i+1:wanted_pos+1] + [element] + input[wanted_pos+1:]
        elif wanted_pos == real_i:
            input = input
        elif wanted_pos < real_i:
            input = input[:wanted_pos] + [element] + input[wanted_pos:real_i] + input[real_i+1:]
    if len(input) != len(input_copy):
        print(wanted_pos, real_i, move_by, len(input))
        exit()
    # try:
    #     input.index((-1987, 4999))
    # except:
    #     print(wanted_pos, real_i, move_by, len(input))
    #     exit()
    # file.write(f'{move_by} ')
    # file.write(str(input))
    # file.write('\n')
    i += 1

file.close()

zero_index = input.index(zero_pair)


result = input[(zero_index+1000)%len(input)][0] + input[(zero_index+2000)%len(input)][0] + input[(zero_index+3000)%len(input)][0]
print("Result: {}".format(result))

#  0, 1,  2, 3,  4, 5, 6
# [1, 2, -3, 3, -2, 0, 4]
#    1, 0,  2, 3,  4, 5, 6
# 1 [2, 1, -3, 3, -2, 0, 4]
#    0,  2, 1, 3,  4, 5, 6
# 2 [1, -3, 2, 3, -2, 0, 4]
# -3 [1, 2, 3, -2, -3, 0, 4]
# 3 [1, 2, -2, -3, 0, 3, 4]
# -2 [1, 2, -3, 0, 3, 4, -2]
# 0 [1, 2, -3, 0, 3, 4, -2]
# 4 [1, 2, -3, 4, 0, 3, -2]