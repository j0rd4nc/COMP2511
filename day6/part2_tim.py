map = open("input.txt", "r").read()
# map = """
# .#..#.....
# .........#
# ..........
# ..........
# ..........
# ..........
# ....^.....
# ........#.
# ..........
# ..........
# """
map = [list(line) for line in map.splitlines()]

m, n = len(map), len(map[0])

r_, c_ = None, None
for r in range(m):
    for c in range(n):
        if map[r][c] not in ['.', '#']:
            r_, c_ = r, c
            break
        
directions = {'>': (0, 1), 'V': (1, 0), '<': (0, -1), '^': (-1, 0)}
next_arrows = {'>': 'V', 'V': '<', '<': '^', '^': '>'}
arrow_ = map[r_][c_]

def print_map():
    for line in map:
        print(''.join(line))

def loop(r, c, arrow):
    """Returns whether map has a loop"""
    dr, dc = directions[arrow]
    steps = set([(r, c, arrow)])

    while True:
        # try taking a step in the direction of the arrow
        nr = r + dr
        nc = c + dc
        
        if 0 <= nr < m and 0 <= nc < n:
            # if obstacle encountered, don't take step, just turn arrow
            if map[nr][nc] == '#':
                arrow = next_arrows[arrow]
                dr, dc = directions[arrow]
            else:
                r, c = nr, nc
                if (r, c, arrow) in steps:
                    return True
                steps.add((r, c, arrow))
        else:
            break
        
    return False


arrow = arrow_
obstacles = set()
r, c = r_, c_

while True:
    dr, dc = directions[arrow]
    
    # try taking a step in the direction of the arrow
    nr = r + dr
    nc = c + dc
    
    if 0 <= nr < m and 0 <= nc < n:
        # if obstacle encountered, don't take step, just turn arrow
        if map[nr][nc] == '#':
            arrow = next_arrows[arrow]
            dr, dc = directions[arrow]
        else:
            # try turning right instead
            map[nr][nc] = '#'
            if loop(r_, c_, arrow_):
                obstacles.add((nr, nc))
            map[nr][nc] = '.'
            
            # regardless of whether that worked, continue            
            r, c = nr, nc
    else:
        break
    
print(obstacles)
print(len(obstacles))