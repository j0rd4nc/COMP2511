from collections import defaultdict

map = open("input.txt", "r").read()
map = map.splitlines()

frequencies = defaultdict(list)
antinode_locations = set()

for i, row in enumerate(map):
    for j, element in enumerate(row):
        if element != ".":
            frequencies[element].append((i, j))
            
max_height = len(map) - 1
max_width = len(map[0]) - 1 

print("max_height", max_height)
print("max_width", max_width)

def check_locations(y, x, y_delta, x_delta, freq):
    while check_location(y, x, freq):
        y += y_delta
        x += x_delta

def check_location(y, x, freq):
    if (y <= max_height and y >= 0 and
        x <= max_width and x >= 0):
        antinode_locations.add((y, x))
        return True

    return False

def check_locations_recursive(y, x, y_delta, x_delta, freq):
    if (y <= max_height and y >= 0 and
        x <= max_width and x >= 0):
        antinode_locations.add((y, x))
        
        check_locations_recursive(y + y_delta, x + x_delta, y_delta, x_delta, freq)    
    
    return

for freq in frequencies:
    antennae = frequencies[freq]
    for i in range(len(antennae)):
        for j in range(i + 1, len(antennae)):
            antenna_i = antennae[i]
            antenna_j = antennae[j]
            
            antenna_i_y = antenna_i[0]
            antenna_i_x = antenna_i[1]
            
            antenna_j_y = antenna_j[0]
            antenna_j_x = antenna_j[1]
            
            y_delta = antenna_i_y - antenna_j_y
            x_delta = antenna_i_x - antenna_j_x
            
            check_locations_recursive(antenna_i_y, antenna_i_x, y_delta, x_delta, freq)
            check_locations_recursive(antenna_i_y, antenna_i_x, -y_delta, -x_delta, freq)
            
            check_locations_recursive(antenna_j_y, antenna_j_x, y_delta, x_delta, freq)
            check_locations_recursive(antenna_j_y, antenna_j_x, -y_delta, -x_delta, freq)

print("result", len(antinode_locations))