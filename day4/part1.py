f = open("input.txt", "r")
lines = []

for line in f:
    lines.append(line)

f.close()

m, n = len(lines), len(lines[0].strip())
print(m, n)

# def find(r, c):    
#     total = 0
    
#     if c + 3 < n:
#         if lines[r][c:c+4] == 'XMAS': # East
#             total += 1
#     if c - 3 >= 0:
#         if lines[r][c-3:c+1] == 'SAMX': # West
#             total += 1
#     if r + 3 < m:
#         if lines[r][c] + lines[r+1][c] + lines[r+2][c] + lines[r+3][c] == 'XMAS': # South
#             total += 1
#     if r - 3 >= 0:
#         if lines[r-3][c] + lines[r-2][c] + lines[r-1][c] + lines[r][c] == 'SAMX': # North
#             total += 1
#     if c + 3 < n and r + 3 < m:
#         if lines[r][c] + lines[r+1][c+1] + lines[r+2][c+2] + lines[r+3][c+3] == 'XMAS': # Southeast
#             total += 1
#     if c + 3 < n and r - 3 >= 0:
#         if lines[r][c] + lines[r-1][c+1] + lines[r-2][c+2] + lines[r-3][c+3] == 'XMAS': # Northeast
#             total += 1
#     if c - 3 >= 0 and r - 3 >= 0:
#         if lines[r][c] + lines[r-1][c-1] + lines[r-2][c-2] + lines[r-3][c-3] == 'XMAS': # Northwest
#             total += 1
#     if c - 3 >= 0 and r + 3 < m:
#         if lines[r][c] + lines[r+1][c-1] + lines[r+2][c-2] + lines[r+3][c-3] == 'XMAS': # Southwest
#             total += 1
    
#     return total

    
# counter = 0
# for r in range(m):
#     output = []
#     for c in range(n):
#         if lines[r][c] == "X":
#            result = find(r, c)
#            counter += result
#            output.append('X' if result > 0 else '.')
#         else:
#             output.append('.')
#             continue
#     print(''.join(output))
       
# print(counter)


directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]

def find(r, c, direction, letters):
    if not letters:
        return True
    dr, dc = direction
    nr, nc = r+dr, c+dc
    if 0 <= nr < m and 0 <= nc < m:
        if lines[nr][nc] == letters[0]:
            return find(nr, nc, direction, letters[1:])
    return False

counter = 0
for r in range(m):
    output = []
    for c in range(n):
        if lines[r][c] == "X":
            for direction in directions:
                counter += find(r, c, direction, 'MAS')
        #     result = find(r, c)
        #    counter += result
        #    output.append('X' if result > 0 else '.')
        else:
            output.append('.')
            continue
    print(''.join(output))
       
print(counter)