map = open("smallinput.txt", "r").read()
map = map.splitlines()

for i, row in enumerate(map):
    for j, element in enumerate(row):
        if element == "^":
            g_y, g_x = i, j
            print(f"Guard found at position ({g_y}, {g_x})")
            break

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

result_set = set()

while True:
    result_set.add((g_y, g_x))
    
    if g_y + 1 >= len(map) or g_y - 1 < 0 or g_x + 1>= len(map[1]) or g_x - 1 < 0:
        break
    elif map[g_y + direction[0]][g_x + direction[1]] == "#":
        direction = change_direction(direction)

    g_y += direction[0]
    g_x += direction[1]
    
print(len(result_set))