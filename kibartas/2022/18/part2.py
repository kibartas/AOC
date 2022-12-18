input = open('input.txt', 'r').read().strip().splitlines()

cubes = []
sides = {}

for line in input:
    x, y, z = line.split(',')
    cube_name = (int(x), int(y), int(z))
    cubes.append(cube_name)
    sides[cube_name] = 6

max_x = 0
max_y = 0
max_z = 0

min_x = 100
min_y = 100
min_z = 100

cube_set = set(cubes)
while True:
    cube = cube_set.pop()
    x_1, y_1, z_1 = cube
    if x_1 < min_x:
        min_x = x_1
    if y_1 < min_y:
        min_y = y_1
    if z_1 < min_z:
        min_z = z_1
    if x_1 > max_x:
        max_x = x_1
    if y_1 > max_y:
        max_y = y_1
    if z_1 > max_z:
        max_z = z_1
    if len(cube_set) == 0:
        break
    for conf in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
        next_cube = (x_1+conf[0], y_1+conf[1], z_1+conf[2])
        if next_cube in cube_set:
            sides[cube] -= 1
            sides[next_cube] -= 1
min_x -= 2
min_y -= 2
min_z -= 2
max_x += 2
max_y += 2
max_z += 2


air_cubes = []
cube_s = set(cubes)
for x in range(min_x, max_x+1):
    for y in range(min_y, max_y+1):
        for z in range(min_z, max_z+1):
            if (x, y, z) not in cube_s:
                air_cubes.append((x, y, z))

def is_free_air_cube(air_cube, free_air_cubes):
    air_x, air_y, air_z = air_cube
    is_free_air = {}
    fake_non_free_air = set()
    for x in reversed(range(min_x, air_x)):
        if (x, air_y, air_z) in cubes:
            is_free_air['x_min'] = (x, air_y, air_z)
            break
        if (x, air_y, air_z) in free_air_cubes:
            fake_non_free_air.add((x, air_y, air_z))
    # if 'x_min' not in is_free_air:
    #     return True, fake_non_free_air
    for x in range(air_x, max_x+1):
        if (x, air_y, air_z) in cubes:
            is_free_air['x_max'] = (x, air_y, air_z)
            break
        if (x, air_y, air_z) in free_air_cubes:
            fake_non_free_air.add((x, air_y, air_z))
    # if 'x_max' not in is_free_air:
    #     return True, fake_non_free_air
    for y in reversed(range(min_y, air_y)):
        if (air_x, y, air_z) in cubes:
            is_free_air['y_min'] = (air_x, y, air_z)
            break
        if (air_x, y, air_z) in free_air_cubes:
            fake_non_free_air.add((air_x, y, air_z))
    # if 'y_min' not in is_free_air:
    #     return True, fake_non_free_air
    for y in range(air_y, max_y+1):
        if (air_x, y, air_z) in cubes:
            is_free_air['y_max'] = (air_x, y, air_z)
            break
        if (air_x, y, air_z) in free_air_cubes:
            fake_non_free_air.add((air_x, y, air_z))
    # if 'y_max' not in is_free_air:
    #     return True, fake_non_free_air
    for z in reversed(range(min_z, air_z)):
        if (air_x, air_y, z) in cubes:
            is_free_air['z_min'] = (air_x, air_y, z)
            break
        if (air_x, air_y, z) in free_air_cubes:
            fake_non_free_air.add((air_x, air_y, z))
    # if 'z_min' not in is_free_air:
    #     return True, fake_non_free_air
    for z in range(air_z, max_z+1):
        if (air_x, air_y, z) in cubes:
            is_free_air['z_max'] = (air_x, air_y, z)
            break
        if (air_x, air_y, z) in free_air_cubes:
            fake_non_free_air.add((air_x, air_y, z))
    # if 'z_max' not in is_free_air:
    #     return True, fake_non_free_air
    if len(is_free_air) != 6:
        return True, fake_non_free_air
    return False, is_free_air


non_free_air_cubes = []
non_free_air_cubes_set = set()
fake_non_free_air_cubes = set()
for air_cube in air_cubes:
    is_free_air, cubes_dict = is_free_air_cube(air_cube, non_free_air_cubes_set)
    if not is_free_air:
        print(air_cube)
        non_free_air_cubes_set.add(air_cube)
        non_free_air_cubes.append((air_cube, cubes_dict))

for air_cube in air_cubes:
    is_free_air, cubes_dict = is_free_air_cube(air_cube, non_free_air_cubes_set)
    if is_free_air:
        fake_non_free_air_cubes |= cubes_dict

print(len(non_free_air_cubes))
print(fake_non_free_air_cubes)

# cube_set = set(cubes)
# fake_non_free_air_cube = fake_non_free_air_cubes.pop()
# fake_non_free_air_cubes.add(fake_non_free_air_cube)
# x_1, y_1, z_1 = fake_non_free_air_cube
# for conf in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
#     next_cube = (x_1+conf[0], y_1+conf[1], z_1+conf[2])
#     if next_cube in non_free_air_cubes_set:
#         print("bazinga")
#     if next_cube in cube_set:
#         print("baringa")
#     if next_cube in air_cubes:
#         print("idk")

while len(fake_non_free_air_cubes) != 0:
    for i, (air_cube, _) in enumerate(non_free_air_cubes):
        if air_cube in fake_non_free_air_cubes:
            non_free_air_cubes = non_free_air_cubes[:i] + non_free_air_cubes[i+1:]
            fake_non_free_air_cubes.remove(air_cube)
            break


cube_sett = set()
for air_cube, non_free_air_cube_dict in non_free_air_cubes:
    for direction, real_cube in non_free_air_cube_dict.items():
        cube_sett.add((direction, real_cube))
print(len(cube_sett))
print(cube_sett)
print(non_free_air_cubes)
print(min_x, max_x, min_y, max_y, min_z, max_z, (8, 6, 18) in cube_set)

result = sum(sides.values()) - len(cube_sett)
print("Result: {}".format(result))
