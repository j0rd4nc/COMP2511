from collections import defaultdict

with open('input.txt', 'r') as file:
    contents = file.read()

contents = contents.splitlines()

equations = []
for line in contents:
    parts = line.replace(":", "").split()
    # Convert each part to an integer
    result = [int(part) for part in parts]
    equations.append(result)

answer = 0

for equation in equations:
    print(equation)
    results = []
    for i in range(1, len(equation)):
        if i == 1:
            results.append(equation[1])
        else:
            for j in range(len(results)):
                temp = results[j]
                results[j] = temp + equation[i]
                results.append(temp * equation[i])

    print(results)
    
    for result in results:
        if result == equation[0]:
            answer += result
            break
            
    print("-----")

print(answer)                