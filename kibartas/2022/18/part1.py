input = open('input.txt', 'r').read().strip().splitlines()

cubes = []
sides = {}

for line in input:
    x, y, z = line.split(',')
    cube_name = (int(x), int(y), int(z))
    cubes.append(cube_name)
    sides[cube_name] = 6

for i in range(len(cubes)-1):
    x_1, y_1, z_1 = cubes[i]
    for j in range(i+1, len(cubes)):
        if ((x_1+1, y_1, z_1) == cubes[j] or (x_1-1, y_1, z_1) == cubes[j] 
            or (x_1, y_1+1, z_1) == cubes[j] or (x_1, y_1-1, z_1) == cubes[j]
            or (x_1, y_1, z_1+1) == cubes[j] or (x_1, y_1, z_1-1) == cubes[j]):
            sides[cubes[i]] -= 1
            sides[cubes[j]] -= 1


print(cubes)
result = sum(sides.values())
print("Result: {}".format(result))
