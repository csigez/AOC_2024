import re

def process_memory(memory_string):
    # Regular expressions for different patterns
    mul_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    do_pattern = r'do\(\)'
    dont_pattern = r'don\'t\(\)'
    
    # Find all instructions with their positions
    mul_matches = [(m.start(), 'mul', m) for m in re.finditer(mul_pattern, memory_string)]
    do_matches = [(m.start(), 'do') for m in re.finditer(do_pattern, memory_string)]
    dont_matches = [(m.start(), 'dont') for m in re.finditer(dont_pattern, memory_string)]
    
    # Combine all matches and sort by position
    all_matches = sorted(mul_matches + do_matches + dont_matches)
    
    total = 0
    enabled = True  # Multiplications are enabled by default
    
    for pos, type_, *args in all_matches:
        if type_ == 'do':
            enabled = True
        elif type_ == 'dont':
            enabled = False
        elif type_ == 'mul' and enabled:
            match = args[0]
            x, y = int(match.group(1)), int(match.group(2))
            total += x * y
    
    return total

# Read input from file
with open('3.txt', 'r') as file:
    memory_string = file.read().strip()

result = process_memory(memory_string)
print(f"Sum of multiplications: {result}")