from itertools import permutations

input = open('input.txt', 'r').read().strip().splitlines()

decimal_arr = []

for line in input:
    print(line)
    multiplier = 1
    decimal = 0
    for i in reversed(range(len(line))):
        chr = line[i]
        if chr.isdigit():
            decimal += multiplier * int(chr)
        elif chr == '-':
            decimal += multiplier * -1
        elif chr == '=':
            decimal += multiplier * -2
        else:
            raise Exception("?")
        multiplier *= 5
    decimal_arr.append(decimal)

final_sum = sum(decimal_arr)

multiplier = 1
pos = 0
while multiplier < final_sum:
    multiplier *= 5
    pos += 1

multiplier //= 5
pos -= 1
print(multiplier, pos, final_sum, final_sum-multiplier * 2)

snafu_number = ''
print(final_sum)
while multiplier != 0:
    if final_sum > 0:
        if abs(final_sum - multiplier) < final_sum:
            candidate = abs(final_sum - multiplier)
            if abs(final_sum - (multiplier * 2)) < final_sum and abs(final_sum - (multiplier * 2)) < candidate:
                snafu_number = snafu_number + '2'
                final_sum -= multiplier * 2
            else:
                snafu_number = snafu_number + '1'
                final_sum -= multiplier
        else:
            snafu_number = snafu_number + '0'
    elif final_sum < 0:
        if abs(final_sum + multiplier) < abs(final_sum):
            candidate = abs(final_sum + multiplier)
            if abs(final_sum + (multiplier * 2)) < abs(final_sum) and abs(final_sum + (multiplier * 2)) < candidate:
                snafu_number = snafu_number + '='
                final_sum += multiplier * 2
            else:
                snafu_number = snafu_number + '-'
                final_sum += multiplier
        else:
            snafu_number = snafu_number + '0'

    print(final_sum, multiplier)
    multiplier //= 5

print(final_sum, multiplier, snafu_number)

result = 0
print("Result: {}".format(result))
