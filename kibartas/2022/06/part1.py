input = open('input.txt', 'r').read().strip()


marker_pos = -1
for i in range(4, len(input)):
    if len(set(input[i-4:i])) == 4:
        marker_pos = i
        break
        

result = marker_pos

print("Result: {}".format(result))
