input = open('input.txt', 'r').read().strip()

binary = format(int(input, 16), '0{}b'.format(len(input)*4))

# 6 is header. If not type 4, then 1 more for length ID.


def parse_packets(packet):
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
            print(packet_count)
            counter = 0
            sub_packets = packet[18:]
            used_bits = 0
            while counter != packet_count:
                literal_value, used_partial, sub_version_sum = parse_packets(
                    sub_packets[used_bits:])
                version_sum += sub_version_sum
                print('literal_value', literal_value)
                used_bits += used_partial
                counter += 1
            return 0, 18+used_bits, version_sum
        elif length_type == '0':
            total_length = int(packet[7:22], 2)
            print(total_length)
            sub_packets = packet[22:22+total_length]
            print(sub_packets)
            used_bits = 0
            while used_bits != len(sub_packets):
                print(used_bits)
                literal_value, used_partial, sub_version_sum = parse_packets(
                    sub_packets[used_bits:])
                version_sum += sub_version_sum
                print('literal_value', literal_value)
                used_bits += used_partial
            return 0, 22+total_length, version_sum
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


_, _, result = parse_packets(binary)
print("Result: {}".format(result))
