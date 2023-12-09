input = open('input.txt', 'r').read().strip().split('\n')

lines = []

for line in input:
    lines.append([int(x) for x in line.split()])

def find_difs(sequence):
    return [sequence[i+1] - sequence[i] for i in range(0, len(sequence)-1)]

sum = 0
for line in lines:
    local_difs = [line]
    while True: 
        local_difs.append(find_difs(local_difs[-1]))
        if local_difs[-1] == len(local_difs[-1]) * [0]:
            for i in range(len(local_difs)-1, -1, -1):
                if i == len(local_difs) - 1:
                    local_difs[i] = [0, *local_difs[i]]
                else:
                    local_difs[i] = [local_difs[i][0] - local_difs[i+1][0], *local_difs[i]]
            sum += local_difs[0][0]
            break

result = sum
print("Result: {}".format(result))
