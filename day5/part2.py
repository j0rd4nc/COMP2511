from collections import defaultdict
import math

puzzle_input = open("input.txt", "r").read()

a, b = puzzle_input.split("\n\n")
a = a.splitlines()
b = b.splitlines()

def build_dd(a, update):
    dd = defaultdict(set)
    update_set = set(update)
    
    for instruction in a:
        value = instruction[0] + instruction[1]
        key = instruction[3] + instruction[4]
        
        if key in update_set and value in update_set:
            dd[key].add(value)
        
    return dd

updates = []
for update in b:
    u = update.split(",")
    updates.append(u)

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

def reorder(update, dd):
    # print("dd", dd)
    
    L = []
    S = set()
    
    for page in update:
        if page not in dd:
            S.add(page)
    
    while S:
        n = S.pop()
        L.append(n)
        
        keys_to_delete = []
        
        # Remove n as a dependency from all keys in the dd
        for key in dd.keys():
            dependencies = dd[key]
            dependencies.discard(n)
            if not dependencies:
                keys_to_delete.append(key)
                S.add(key)
                
        for key in keys_to_delete:
            del dd[key]  
    
    return L
                
correctly_ordered = []
incorrectly_ordered = []
for update in updates:
    dd = build_dd(a, update)
    
    # if check_update_is_ordered(update, dd):
    #     correctly_ordered.append(update)
    # else:
    L = reorder(update, dd)
    if L != update:
        incorrectly_ordered.append(L)
    print("update", update)
    print("L", L)
    print("---")

result = 0
for list in incorrectly_ordered:
    result += int(list[math.ceil(len(list)/2) - 1])

print(result)

