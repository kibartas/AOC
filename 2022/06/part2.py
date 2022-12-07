input = open('input.txt', 'r').read().strip()


marker_pos = -1
for i in range(14, len(input)):
    if len(set(input[i-14:i])) == 14:
        marker_pos = i
        break
        

result = marker_pos

print("Result: {}".format(result))
