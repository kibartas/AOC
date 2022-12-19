import time
import functools
input = open('input.txt', 'r').read().strip().splitlines()
print(input)

blueprints = {}

for i, line in enumerate(input):
    _, _, _, _, _, _, ore_cost, _, _, _, _, _, clay_cost, _, _, _, _, _, obsidian_ore_cost, _, _, obsidian_clay_cost, _, _, _, _, _, geode_ore_cost, _, _, geode_obsidian_cost, _ = line.split()
    blueprints[i+1] = (int(ore_cost), int(clay_cost), int(obsidian_ore_cost), int(obsidian_clay_cost), int(geode_ore_cost), int(geode_obsidian_cost), max(int(ore_cost), int(clay_cost), int(obsidian_ore_cost), int(geode_ore_cost)))
    
print(blueprints)

time_limit = 24
robot_counts = (1, 0, 0, 0)
resource_counts = (0, 0, 0, 0)

def collect_resources(resource_counts, robot_counts):
    return (resource_counts[0]+robot_counts[0], resource_counts[1]+robot_counts[1], resource_counts[2]+robot_counts[2], resource_counts[3]+robot_counts[3])

@functools.cache
def get_sum(start, n, increase):
    d_0 = 1
    d = increase
    return (d_0 * n**2) / 2 + (d - (3*d_0)/2) * n + (d_0 + start - d)

maximum_geod = 0

@functools.cache
def naive_work(time_limit=32, blueprint=2, robot_counts=robot_counts, resource_counts=resource_counts):
    global maximum_geod
    if (get_sum(robot_counts[2], time_limit+2, robot_counts[2]+1) + resource_counts[2] < blueprints[blueprint][5]) or (get_sum(robot_counts[1], time_limit+1, robot_counts[1]+1) + resource_counts[1] < blueprints[blueprint][3]) or (get_sum(robot_counts[0], time_limit+2, robot_counts[0]+1) + resource_counts[0] < blueprints[blueprint][4]) or (get_sum(robot_counts[3], time_limit+2, robot_counts[3]+1) + resource_counts[3] < maximum_geod):
        return 0
    if time_limit == 0:
        if resource_counts[3] > maximum_geod:
            maximum_geod = resource_counts[3]
        return resource_counts[3]
    new_resource_counts = collect_resources(resource_counts, robot_counts)
    results = []
    if resource_counts[0] >= blueprints[blueprint][4] and resource_counts[2] >= blueprints[blueprint][5]:
        new_robot_counts = (robot_counts[0], robot_counts[1], robot_counts[2], robot_counts[3]+1)
        inner_new_resource_counts = (new_resource_counts[0]-blueprints[blueprint][4], new_resource_counts[1], new_resource_counts[2]-blueprints[blueprint][5], new_resource_counts[3])
        results.append(naive_work(time_limit-1, blueprint, new_robot_counts, inner_new_resource_counts))
    elif resource_counts[0] >= blueprints[blueprint][2] and resource_counts[1] >= blueprints[blueprint][3] and robot_counts[2] <= blueprints[blueprint][5] // 2 + 1:
        new_robot_counts = (robot_counts[0], robot_counts[1], robot_counts[2]+1, robot_counts[3])
        inner_new_resource_counts = (new_resource_counts[0]-blueprints[blueprint][2], new_resource_counts[1]-blueprints[blueprint][3], new_resource_counts[2], new_resource_counts[3])
        results.append(naive_work(time_limit-1, blueprint, new_robot_counts, inner_new_resource_counts))
    elif resource_counts[0] >= blueprints[blueprint][1] and robot_counts[1] <= blueprints[blueprint][3] // 2 + 1:
        new_robot_counts = (robot_counts[0], robot_counts[1]+1, robot_counts[2], robot_counts[3])
        inner_new_resource_counts = (new_resource_counts[0]-blueprints[blueprint][1], new_resource_counts[1], new_resource_counts[2], new_resource_counts[3])
        results.append(naive_work(time_limit-1, blueprint, new_robot_counts, inner_new_resource_counts))
    elif resource_counts[0] >= blueprints[blueprint][0] and robot_counts[0] <= blueprints[blueprint][-1] // 2 + 1:
        new_robot_counts = (robot_counts[0]+1, robot_counts[1], robot_counts[2], robot_counts[3])
        inner_new_resource_counts = (new_resource_counts[0]-blueprints[blueprint][0], new_resource_counts[1], new_resource_counts[2], new_resource_counts[3])
        results.append(naive_work(time_limit-1, blueprint, new_robot_counts, inner_new_resource_counts))
    else:
        results.append(naive_work(time_limit-1, blueprint, robot_counts, new_resource_counts)) 

    return max(results)


@functools.cache
def work(time_limit=32, blueprint=2, robot_counts=robot_counts, resource_counts=resource_counts):
    global maximum_geod
    if (get_sum(robot_counts[2], time_limit+2, robot_counts[2]+1) + resource_counts[2] < blueprints[blueprint][5]) or (get_sum(robot_counts[1], time_limit+1, robot_counts[1]+1) + resource_counts[1] < blueprints[blueprint][3]) or (get_sum(robot_counts[0], time_limit+2, robot_counts[0]+1) + resource_counts[0] < blueprints[blueprint][4]) or (get_sum(robot_counts[3], time_limit+2, robot_counts[3]+1) + resource_counts[3] < maximum_geod):
        return 0
    if time_limit == 0:
        if resource_counts[3] > maximum_geod:
            maximum_geod = resource_counts[3]
        return resource_counts[3]
    new_resource_counts = collect_resources(resource_counts, robot_counts)
    results = []
    counter = 0
    if resource_counts[0] >= blueprints[blueprint][4] and resource_counts[2] >= blueprints[blueprint][5]:
        new_robot_counts = (robot_counts[0], robot_counts[1], robot_counts[2], robot_counts[3]+1)
        inner_new_resource_counts = (new_resource_counts[0]-blueprints[blueprint][4], new_resource_counts[1], new_resource_counts[2]-blueprints[blueprint][5], new_resource_counts[3])
        results.append(work(time_limit-1, blueprint, new_robot_counts, inner_new_resource_counts))
    else:
        for i in range(4):
            if i == 0 and resource_counts[0] >= blueprints[blueprint][0] and robot_counts[i] <= blueprints[blueprint][-1] // 2 + 1:
                new_robot_counts = (robot_counts[0]+1, robot_counts[1], robot_counts[2], robot_counts[3])
                inner_new_resource_counts = (new_resource_counts[0]-blueprints[blueprint][i], new_resource_counts[1], new_resource_counts[2], new_resource_counts[3])
                results.append(work(time_limit-1, blueprint, new_robot_counts, inner_new_resource_counts))
                counter += 1
            elif i == 1 and resource_counts[0] >= blueprints[blueprint][1] and robot_counts[i] <= blueprints[blueprint][3] // 2 + 1:
                new_robot_counts = (robot_counts[0], robot_counts[1]+1, robot_counts[2], robot_counts[3])
                inner_new_resource_counts = (new_resource_counts[0]-blueprints[blueprint][i], new_resource_counts[1], new_resource_counts[2], new_resource_counts[3])
                results.append(work(time_limit-1, blueprint, new_robot_counts, inner_new_resource_counts))
                counter += 1
            elif i == 2 and resource_counts[0] >= blueprints[blueprint][2] and resource_counts[1] >= blueprints[blueprint][3] and robot_counts[i] <= blueprints[blueprint][5] // 2 + 1:
                new_robot_counts = (robot_counts[0], robot_counts[1], robot_counts[2]+1, robot_counts[3])
                inner_new_resource_counts = (new_resource_counts[0]-blueprints[blueprint][2], new_resource_counts[1]-blueprints[blueprint][3], new_resource_counts[2], new_resource_counts[3])
                results.append(work(time_limit-1, blueprint, new_robot_counts, inner_new_resource_counts))
                counter += 1

        if counter != 3:
            results.append(work(time_limit-1, blueprint, robot_counts, new_resource_counts)) 
    return max(results)

start = time.time()
result = 1
assert get_sum(0, 3, 1) == 3
assert get_sum(1, 2, 2) == 3
assert get_sum(1, 2, 2) == 3
assert get_sum(1, 3, 2) == 6
assert get_sum(3, 3, 3) == 10
for id in blueprints.keys():
    if id == 4:
        break
    naive_work(time_limit=32, blueprint=id)
    print(maximum_geod)
    quality = work(time_limit=32, blueprint=id) 
    maximum_geod = 0
    print(id, quality)
    result *= quality
    print(f'after {id}: {time.time()-start}')
print("Result: {} {}".format(result, time.time()-start))
