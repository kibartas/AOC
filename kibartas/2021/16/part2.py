import numpy as np

input = open('input.txt', 'r').read().strip()

binary = format(int(input, 16), '0{}b'.format(len(input)*4))

# 6 is header. If not type 4, then 1 more for length ID.


def parse_packets(packet):
    print(packet)
    version = int(packet[0:3], 2)
    version_sum = version
    print('version_sum', version_sum)
    packet_type = int(packet[3:6], 2)
    print('type', packet_type)
    if packet_type != 4:
        length_type = packet[6:7]
        print('length type', length_type)
        if length_type == '1':
            packet_count = int(packet[7:18], 2)
            print('packet_count', packet_count)
            counter = 0
            sub_packets = packet[18:]
            used_bits = 0
            literal_values = []
            while counter != packet_count:
                literal_value, used_partial, sub_sum = parse_packets(
                    sub_packets[used_bits:])
                print('literal_value', literal_value)
                version_sum += sub_sum
                used_bits += used_partial
                literal_values.append(literal_value)
                counter += 1
                print(counter, packet_count)
            print(literal_values)
            if packet_type == 0:
                return sum(literal_values), 18+used_bits, version_sum
            elif packet_type == 1:
                return np.prod(literal_values), 18+used_bits, version_sum
            elif packet_type == 2:
                return min(literal_values), 18+used_bits, version_sum
            elif packet_type == 3:
                return max(literal_values), 18+used_bits, version_sum
            elif packet_type == 5:
                return 1 if literal_values[0] > literal_values[1] else 0, 18+used_bits, version_sum
            elif packet_type == 6:
                return 1 if literal_values[0] < literal_values[1] else 0, 18+used_bits, version_sum
            elif packet_type == 7:
                print(literal_values)
                return 1 if literal_values[0] == literal_values[1] else 0, 18+used_bits, version_sum
        elif length_type == '0':
            total_length = int(packet[7:22], 2)
            print('total_length', total_length)
            sub_packets = packet[22:22+total_length]
            print(sub_packets)
            used_bits = 0
            literal_values = []
            while used_bits != len(sub_packets):
                print(used_bits)
                literal_value, used_partial, sub_sum = parse_packets(
                    sub_packets[used_bits:])
                version_sum += sub_sum
                print('literal_value', literal_value)
                literal_values.append(literal_value)
                used_bits += used_partial
            print(literal_values, packet_type)
            if packet_type == 0:
                return sum(literal_values), 22+total_length, version_sum
            elif packet_type == 1:
                return np.prod(literal_values), 22+total_length, version_sum
            elif packet_type == 2:
                return min(literal_values), 22+total_length, version_sum
            elif packet_type == 3:
                return max(literal_values), 22+total_length, version_sum
            elif packet_type == 5:
                return 1 if literal_values[0] > literal_values[1] else 0, 22+total_length, version_sum
            elif packet_type == 6:
                return 1 if literal_values[0] < literal_values[1] else 0, 22+total_length, version_sum
            elif packet_type == 7:
                print("HELLOOO")
                if literal_values[0] == literal_values[1]:
                    return 1, 22+total_length, version_sum
                return 1 if literal_values[0] == literal_values[1] else 0, 22+total_length, version_sum
    else:
        number = ''
        used_bits = 0
        print('packet', packet)
        for i in range(6, len(packet), 5):
            number += packet[i+1:i+5]
            if packet[i] == '0':
                used_bits = i+5
                break
        literal_value = int(number[:], 2)
        return literal_value, used_bits, version_sum


result, _, version_sum = parse_packets(binary)
print(version_sum)
print("Result: {}".format(result))
