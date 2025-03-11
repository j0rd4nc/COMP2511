f = open("input.txt", "r")
lines = []

for line in f:
    lines.append(line)

f.close()

m, n = len(lines), len(lines[0].strip())

def find(r, c):
    if r - 1 >= 0 and r + 1 < m and c - 1 >= 0 and c + 1 < n:
        if (lines[r-1][c-1] + lines[r][c] + lines[r+1][c+1] == 'MAS' or
            lines[r-1][c-1] + lines[r][c] + lines[r+1][c+1] == 'SAM'):
            if (lines[r+1][c-1] + lines[r][c] + lines[r-1][c+1] == 'MAS' or
                lines[r+1][c-1] + lines[r][c] + lines[r-1][c+1] == 'SAM'):
                return 1
    
    return 0

    
counter = 0
for r in range(m):
    output = []
    for c in range(n):
        if lines[r][c] == "A":
           result = find(r, c)
           counter += result
           output.append('X' if result > 0 else '.')
        else:
            output.append('.')
            continue
       
print(counter)