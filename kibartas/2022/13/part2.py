from functools import cmp_to_key

input = open('input.txt', 'r').read().strip().splitlines()

packets = [el for el in input if el != '']
packets.append('[[2]]')
packets.append('[[6]]')

def get_number(packet, i):
    number = ''
    while packet[i].isnumeric():
        number += packet[i]
        i += 1
    return int(number), i

def compare_lists(left, right, i=0, j=0):
    i += 1
    j += 1
    while i < len(left):
        print(left, right, i, j, left[i], right[j])
        if left[i] == '[' and right[j] == '[':
            result = compare_lists(left, right, i, j)
            if isinstance(result, int):
                return result
            else:
                i, j = result
            i += 1
            j += 1
        elif left[i] == ',' and right[j] == ',':
            i += 1
            j += 1
        elif left[i] == ',':
            i += 1
        elif right[j] == ',':
            j += 1
        elif left[i].isnumeric() and right[j].isnumeric():
            left_number, i = get_number(left, i)
            right_number, j = get_number(right, j)
            # print(left_number < right_number)
            if left_number > right_number:
               return -1
            elif left_number < right_number:
                return 1
        elif left[i] != ']' and right[j] == ']':
            # right ran out of things to compare
            return -1
        elif left[i] == ']' and right[j] != ']':
            # left ran out of things to compare
            return 1
        elif left[i] == ']' and right[j] == ']':
            # both are equal, return new indices
            return i, j
        elif left[i].isnumeric() and right[j] == '[':
            left_number, i = get_number(left, i)
            left_list = str([left_number])
            result = compare_lists(left_list, right, 0, j)
            if isinstance(result, int):
                return result
        elif left[i] == '[' and right[j].isnumeric():
            right_number, j = get_number(right, j)
            right_list = str([right_number])
            result = compare_lists(left, right_list, i, 0)
            if isinstance(result, int):
                return result

    # left ran out of things to compare
    return True

        

packets.sort(key=cmp_to_key(compare_lists), reverse=True)
result = 1
for i, packet in enumerate(packets):
    if packet == '[[2]]' or packet == '[[6]]':
        result *= i + 1
print("Result: {}".format(result))


# 39 
# '[[7,9,9,[[7,6],8],5],[0,10,[3,5,1,[0,10,1,8]]],[[[10]],[8,[2,0,10,9,1],7,[8,1,7],[0,8,3]]],[[9,[0,0,9,3],[5,0,10,7,10]],[],[10,7],[],[[10,6,10],[10,3,4,8],1,[]]],[3,[],[[],[7,10],0],[]]]' 
# '[[[7]]]'