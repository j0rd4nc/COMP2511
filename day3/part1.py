import re

pattern = r"mul\((\d+),(\d+)\)"

with open("input.txt", "r") as file:
    text = file.read()

matches = re.findall(pattern, text)

total = 0
for match in matches:
    a, b = map(int, match)
    total += a * b

print(total)