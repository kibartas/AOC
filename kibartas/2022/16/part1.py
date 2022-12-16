input = open('input.txt', 'r').read().strip().splitlines()

graph = {}

time_left = 30

for line in input:
    line_split = line.split()
    node = line_split[1]
    flow = int(line_split[4].split('=')[1].rstrip(';'))
    next_nodes = [x.rstrip(',') for x in line_split[9:]]
    graph[node] = (next_nodes, flow)

non_zero_valves_with_flow = []
non_zero_valves = set()
for node, (_, flow) in graph.items():
    if flow != 0:
        non_zero_valves_with_flow.append((node, flow))
        non_zero_valves.add(node)

print(non_zero_valves_with_flow)
non_zero_valves_with_flow.sort(key=lambda x: x[1], reverse=True)
current_max = 0

def is_there_a_loop(road):
    # ex. AA->DD->AA->DD 
    road_in_parts = road.split('->')
    if len(road_in_parts) < 4:
        return False
    for i in range(len(road_in_parts)-3):
        if road_in_parts[i] == road_in_parts[i+2] and road_in_parts[i+1] == road_in_parts[i+3]:
            return True
    return False

def calculate_left(nodes, time_left):
    pressure_left = 0
    for non_zero_valve in non_zero_valves_with_flow:
        if non_zero_valve in nodes:
            continue    
        pressure_left += non_zero_valve[1] * time_left
        time_left -= 2
        if time_left <= 0:
            break
    return pressure_left
        
        

def traverse_graph(current_node='AA', time_left=30, pressure_released=0, valves_opened=[], road='AA'):
    global current_max
    if is_there_a_loop(road):
        return 0
    if road == 'AA->DD->CC->BB->AA->II->JJ->II->AA->DD' and pressure_released == 1326:
        print("HEY", pressure_released, current_node, valves_opened, time_left-1, current_max, calculate_left(valves_opened, time_left), road)

    if pressure_released + calculate_left(valves_opened, time_left) < current_max:
        return 0
    # if len(valves_opened) > 0 and valves_opened[0] == 'DD' and pressure_released == 1326:
    #     # print(pressure_released, current_node, valves_opened, time_left-1, flow, current_max, calculate_left(valves_opened, time_left))
    #     print(pressure_released, current_node, valves_opened, time_left-1, current_max, calculate_left(valves_opened, time_left), road)
    if time_left - 1 == 0 or len(valves_opened) == len(non_zero_valves):
        if pressure_released > current_max:
            current_max = pressure_released
        return pressure_released
    results = []
    # opening the valve
    if current_node in non_zero_valves and current_node not in valves_opened:
        flow = graph[current_node][1]
        new_pressure_released = pressure_released + (time_left-1) * flow
        if time_left - 2 == 0:
            if new_pressure_released > current_max:
                current_max = new_pressure_released
            return new_pressure_released
        for next_node in graph[current_node][0]:
            # if current_node + '->' + next_node in road:
            #     continue
            if next_node in non_zero_valves:
                results.append(traverse_graph(next_node, time_left-2, new_pressure_released, valves_opened + [current_node], road + '->' + next_node))
        for next_node in graph[current_node][0]:
            # if current_node + '->' + next_node in road:
            #     continue
            if next_node not in non_zero_valves:
                results.append(traverse_graph(next_node, time_left-2, new_pressure_released, valves_opened + [current_node], road + '->' + next_node))
    # not opening the valve
    for next_node in graph[current_node][0]:
        # if current_node + '->' + next_node in road:
        #     continue
        if next_node in non_zero_valves:
            results.append(traverse_graph(next_node, time_left-1, pressure_released, valves_opened, road + '->' + next_node))
    for next_node in graph[current_node][0]:
        # if current_node + '->' + next_node in road:
        #     continue
        if next_node not in non_zero_valves:
            results.append(traverse_graph(next_node, time_left-1, pressure_released, valves_opened, road + '->' + next_node))
    return max(results) if len(results) != 0 else 0
        
        
# AA -> II ! [AA, None, None]
# II -> AA ! [AA, II, None]
# AA -> II X [AA, II, AA]

# [AA, II]
# [II, AA]

result = traverse_graph()
print("Result: {}".format(result))
