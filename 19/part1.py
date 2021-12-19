from itertools import permutations
input = open('input.txt', 'r').read().strip().split('\n\n')
all_beacons = open('all_beacons.txt').read().split('\n')

beacons = set()
for i, beacon in enumerate(all_beacons):
    split = beacon.split(',')
    x = int(split[0])
    y = int(split[1])
    z = int(split[2])
    beacons.add((x, y, z))


scanners = []

for i, scanner in enumerate(input):
    coordinates = scanner.split('\n')[1:]
    scanners.append([])
    for coordinate in coordinates:
        split = coordinate.split(',')
        x = int(split[0])
        y = int(split[1])
        z = int(split[2])
        scanners[i].append((x, y, z))


def calculate_orientations(scanners):
    orientations = []
    for j, scanner in enumerate(scanners):
        orientations.append([])
        for coordinates in scanner:
            permutations_with_signs = []
            for permutation in permutations(coordinates):
                permutations_with_signs.append(permutation)
                permutations_with_signs.append(
                    (-permutation[0], -permutation[1], -permutation[2]))
                permutations_with_signs.append(
                    (-permutation[0], -permutation[1], permutation[2]))
                permutations_with_signs.append(
                    (-permutation[0], permutation[1], permutation[2]))
                permutations_with_signs.append(
                    (-permutation[0], permutation[1], -permutation[2]))
                permutations_with_signs.append(
                    (permutation[0], -permutation[1], -permutation[2]))
                permutations_with_signs.append(
                    (permutation[0], -permutation[1], permutation[2]))
                permutations_with_signs.append(
                    (permutation[0], permutation[1], -permutation[2]))
            for i, permutation_with_sign in enumerate(permutations_with_signs):
                if i < len(orientations[j]):
                    orientations[j][i].append(permutation_with_sign)
                else:
                    orientations[j].append([permutation_with_sign])
    return orientations


orientations = calculate_orientations(scanners)
found_beacons = set(scanners[0])
found_beacons_last = 0
positions = {0: (0, 0, 0)}
while len(positions.keys()) != len(scanners):
    print('have scanners: ', sorted(positions.keys()))
    for j in range(1, len(scanners)):
        for beacon_to_find in found_beacons:
            found = False
            for orientation in orientations[j]:
                for coordinates in orientation:
                    diff_x = beacon_to_find[0] - coordinates[0]
                    diff_y = beacon_to_find[1] - coordinates[1]
                    diff_z = beacon_to_find[2] - coordinates[2]
                    counter = 0
                    all_of_them = []
                    for more in orientation:
                        candidate = (more[0] + diff_x, more[1] +
                                     diff_y, more[2] + diff_z)
                        all_of_them.append(candidate)
                        if candidate in found_beacons:
                            counter += 1
                    if counter >= 12:
                        found_beacons = found_beacons.union(
                            set(all_of_them))
                        if j not in positions.keys():
                            positions[j] = (diff_x, diff_y, diff_z)
                        found = True
                        break
                if found:
                    break
            if found:
                break

result = len(found_beacons)
print(positions)
print("Result: {}".format(result))
