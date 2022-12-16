import time
from collections import deque

input = open('input.txt', 'r').read().strip().splitlines()

start = time.time()
graph = {}
dead_ends = set()

for line in input:
    line_split = line.split()
    node = line_split[1]
    flow = int(line_split[4].split('=')[1].rstrip(';'))
    next_nodes = [x.rstrip(',') for x in line_split[9:]]
    graph[node] = (next_nodes, flow)
    if len(next_nodes) == 1:
        dead_ends.add(node)

print(dead_ends)

def breadth_first(goal, root):
    q = deque()
    explored = {root}
    parents = {}
    q.append(root)
    while len(q) != 0:
        current_node = q.popleft()
        if current_node == goal:
            return parents
        for next_node in graph[current_node][0]:
            if next_node not in explored:
                explored.add(next_node)
                parents[next_node] = current_node
                q.append(next_node)

non_zero_valves_with_flow = []
non_zero_valves = set()
for node, (_, flow) in graph.items():
    if flow != 0:
        non_zero_valves_with_flow.append((node, flow))
        non_zero_valves.add(node)

non_zero_valves_with_flow.sort(key=lambda x: x[1], reverse=True)
print(non_zero_valves_with_flow, len(non_zero_valves_with_flow))
current_max = 0

def is_there_a_loop(road):
    if len(road) < 14:
        return False
    if len(road) >= 14:
        # ex. AA->DD->AA->DD 
        i = len(road) - 14
        if road[i:i+6] == road[i+8:i+15]:
            return True
    if len(road) >= 22:
        # ex. AA->DD->CC->AA->DD->CC
        i = len(road) - 22
        if road[i:i+10] == road[i+12:i+22]:
            return True
    if len(road) >= 30:
        # ex. AA->BB->CC->DD->AA->BB->CC->DD
        i = len(road) - 30
        if road[i:i+14] == road[i+16:i+30]:
            return True
    return False

assert is_there_a_loop('AA->DD->AA->DD') is True
assert is_there_a_loop('AA->DD->CC->AA->DD->CC') is True
assert is_there_a_loop('AA->BB->CC->DD->AA->BB->CC->DD') is True

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

roads = {}
def get_roads():
    for node in non_zero_valves | {'AA'}:
        for valve in non_zero_valves_with_flow:
            if valve[0] == node:
                continue
            parents = breadth_first(valve[0], node)
            road_length = 0
            goal = node
            current_node = valve[0]
            road = [valve[0]]
            while current_node != goal:
                current_node = parents[current_node]
                road_length += 1
                road = [current_node] + road
            roads[(node, valve[0])] = len(road)
    
get_roads()

current_max = 0


def traverse(current_node='AA', second_current_node='AA', time_left=26, el_time_left=26, pressure_released=0, opened=set()):
    global current_max
    if pressure_released > current_max:
        current_max = pressure_released
    if opened == non_zero_valves or (time_left == 0 and el_time_left == 0):
        return
    # both make moves
    if time_left == el_time_left:
        for valve in non_zero_valves_with_flow:
            if valve[0] == current_node:
                continue
            new_time_left = time_left - roads[(current_node, valve[0])]
            new_pressure_released = valve[1] * new_time_left
            if new_time_left < 0 or valve[0] in opened:
                continue
            for el_valve in non_zero_valves_with_flow:
                if el_valve[0] == second_current_node or valve[0] == el_valve[0]:
                    continue 
                el_new_time_left = el_time_left - roads[(second_current_node, el_valve[0])]
                if el_new_time_left < 0 or el_valve[0] in opened:
                    continue
                el_pressure_released = el_valve[1] * el_new_time_left
                traverse(valve[0], el_valve[0], new_time_left, el_new_time_left, pressure_released + new_pressure_released + el_pressure_released, opened | {valve[0]} | {el_valve[0]})
    # I make the move
    elif time_left > el_time_left:
        for valve in non_zero_valves_with_flow:
            if valve[0] == current_node:
                continue
            new_time_left = time_left - roads[(current_node, valve[0])]
            new_pressure_released = valve[1] * new_time_left
            if new_time_left < 0 or valve[0] in opened:
                continue
            traverse(valve[0], second_current_node, new_time_left, el_time_left, pressure_released + new_pressure_released, opened | {valve[0]})
    # elephant makes move first
    elif time_left < el_time_left:
        for el_valve in non_zero_valves_with_flow:
            if el_valve[0] == second_current_node:
                continue
            el_new_time_left = el_time_left - roads[(second_current_node, el_valve[0])]
            el_new_pressure_released = el_valve[1] * el_new_time_left
            if el_new_time_left < 0 or el_valve[0] in opened:
                continue
            traverse(current_node, el_valve[0], time_left, el_new_time_left, pressure_released + el_new_pressure_released, opened | {el_valve[0]})


print(roads)
traverse()
        
# AA -> II ! [AA, None, None]
# II -> AA ! [AA, II, None]
# AA -> II X [AA, II, AA]

# [AA, II]
# [II, AA]
# traverse_graph()
result = current_max
print("Result: {}".format(result), time.time() - start)
