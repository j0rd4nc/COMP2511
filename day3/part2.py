import re

# Define the regex patterns to match
patterns = {
    "mul": r"mul\((\d+),(\d+)\)",  # Matches mul(a,b)
    "do": r"do\(\)",              # Matches do()
    "dont": r"don't\(\)"           # Matches dont()
}
compiled_patterns = {key: re.compile(pattern) for key, pattern in patterns.items()}

# File path to read
file_path = "input.txt"

# Buffer to hold the current window of characters
buffer = ""

enabled = True
total = 0

with open(file_path, "r") as file:
    while True:
        char = file.read(1)  # Read one character at a time
        if not char:  # End of file
            break

        buffer += char  # Add the character to the buffer
        
        # Check for matches in the buffer
        for key, regex in compiled_patterns.items():
            match = regex.search(buffer)
            if match:
            
                if key == "mul" and enabled == True:
                    # Extract integers if it's a "mul" pattern
                    a, b = map(int, match.groups())
                    total += a * b

                if key == "do":
                    enabled = True
                
                if key == "dont":
                    enabled = False
                
                # Remove the matched part from the buffer
                buffer = buffer[match.end():]
                break  # Exit the loop to avoid re-checking after a match

print(total)