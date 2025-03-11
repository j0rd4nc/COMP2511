map = open("smallinput.txt", "r").read()
map = map.splitlines()

for i, row in enumerate(map):
    for j, element in enumerate(row):
        if element == "^":
            g_y, g_x = i, j
            print(f"Guard found at position ({g_y}, {g_x})")
            break

original_y, original_x = g_y, g_x
map  = [list(string) for string in map]

direction = [-1, 0]

def change_direction(direction):
    if direction == [1, 0]: # down
        return [0, -1] # go left
    elif direction == [0, 1]: # right
        return [1, 0] # go down
    elif direction == [-1, 0]: # up
        return [0, 1] # go right
    elif direction == [0, -1]: # # left
        return [-1, 0] # go up
    
def find_loop(map, g_y, g_x, direction):    
    obstacles = 0
    init_direction = direction
    
    init_y = g_y
    init_x = g_x
    
    stop_at_y = -1
    stop_at_x = -1
    
    while True:
        if obstacles == 3:
            if init_direction == [-1, 0] or init_direction == [1, 0]:
                stop_at_y = g_y
                stop_at_x = init_x
                
            elif init_direction == [0, 1] or init_direction == [0, -1]:
                stop_at_y = init_y
                stop_at_x = g_x
                        
            if g_y == stop_at_y and g_x == stop_at_x:
                print("stop y", stop_at_y)
                print("stop x", stop_at_x)
                print("---")
                return True
            
        if g_y + 1 >= len(map) or g_y - 1 < 0 or g_x + 1>= len(map[1]) or g_x - 1 < 0:
            return False
        elif map[g_y + direction[0]][g_x + direction[1]] == "#":
            direction = change_direction(direction)
            obstacles += 1
            
            if obstacles > 3:
                return False
        
        g_y += direction[0]
        g_x += direction[1]

unique_positions = set()

loops_found = 0
while True:
    if direction == [1, 0] or direction == [-1, 0]:
        if map[g_y][g_x] == "-":
            map[g_y][g_x] = "+"
        else:
            map[g_y][g_x] = "|"
    elif direction == [0, 1] or direction == [0, -1]:
        if map[g_y][g_x] == "|":
            map[g_y][g_x] = "+"
        else:
            map[g_y][g_x] = "-"
    
    if g_y + 1 >= len(map) or g_y - 1 < 0 or g_x + 1>= len(map[1]) or g_x - 1 < 0:
        break
    elif map[g_y + direction[0]][g_x + direction[1]] == "#":
        if find_loop(map, g_y, g_x, direction):
            loops_found += 1
        
        direction = change_direction(direction)
        map[g_y][g_x] = "+"

    g_y += direction[0]
    g_x += direction[1]

map[original_y][original_x] = "^"
    
for row in map:
    print(row)
    
print(loops_found)