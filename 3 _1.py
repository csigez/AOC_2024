import re

def process_memory(memory_string):
    # Regular expression to match valid mul(X,Y) patterns
    # Matches: mul( followed by 1-3 digits, then comma, then 1-3 digits, then )
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    
    # Find all valid matches
    matches = re.finditer(pattern, memory_string)
    
    total = 0
    for match in matches:
        x, y = int(match.group(1)), int(match.group(2))
        total += x * y
    
    return total

# Read input from file
with open('3.txt', 'r') as file:
    memory_string = file.read().strip()

result = process_memory(memory_string)
print(f"Sum of multiplications: {result}")