from collections import defaultdict
import math

puzzle_input = open("input.txt", "r").read()

a, b = puzzle_input.split("\n\n")
a = a.splitlines()
b = b.splitlines()

dd = defaultdict(set)

for instruction in a:
    x, y = instruction.split('|')
    dd[x].add(y)
    
    
result = 0
for manual in b:
    manual = manual.split(',')
    if len(set(manual)) < len(manual):
        continue
    
    l = set()
    for e in manual:
        if len(dd[e].intersection(l)) > 0:
            break
        l.add(e)
    else:
        result += int(manual[len(manual) // 2])
        
print(result)
    
    # break

# dd = defaultdict(list)

# for instruction in a:
#     key = instruction[0] + instruction[1]
#     value = instruction[3] + instruction[4]
#     dd[key].append(value)

# updates = []
# for update in b:
#     u = update.split(",")
#     updates.append(u)

# def check_update_is_ordered(update, dd):
#     for page in update:
#         for value in dd[page]:
#             if update.count(value) > 0:
#                 if update.index(value) > update.index(page):
#                     continue
#                 else:
#                     return False
#             else:
#                 continue
    
#     return True
                
# correctly_ordered = []
# for update in updates:
#     if check_update_is_ordered(update, dd):
#         correctly_ordered.append(update)
        
# print(correctly_ordered)

# result = 0
# for list in correctly_ordered:
#     result += int(list[math.ceil(len(list)/2) - 1])

# print(result)

