def is_safe_report(levels):
    if len(levels) < 2:
        return True
    
    # Check if the sequence is strictly increasing or decreasing
    differences = [levels[i+1] - levels[i] for i in range(len(levels)-1)]
    
    # All differences should be in the same direction (all positive or all negative)
    if not (all(d > 0 for d in differences) or all(d < 0 for d in differences)):
        return False
    
    # Check if differences are between 1 and 3
    return all(1 <= abs(d) <= 3 for d in differences)

def is_safe_with_dampener(levels):
    # First check if it's safe without dampener
    if is_safe_report(levels):
        return True
    
    # Try removing each level one at a time
    for i in range(len(levels)):
        # Create a new list without the current level
        dampened_levels = levels[:i] + levels[i+1:]
        if is_safe_report(dampened_levels):
            return True
    
    return False

def count_safe_reports(filename, use_dampener=False):
    safe_count = 0
    try:
        with open(filename, 'r') as file:
            for line in file:
                # Convert each line to a list of integers
                levels = [int(x) for x in line.strip().split()]
                if use_dampener:
                    if is_safe_with_dampener(levels):
                        safe_count += 1
                else:
                    if is_safe_report(levels):
                        safe_count += 1
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
        return 0
    except Exception as e:
        print(f"Error processing file: {e}")
        return 0
    
    return safe_count

# Part 1: Without Problem Dampener
result_without_dampener = count_safe_reports('2.txt', use_dampener=False)
print(f"Part 1 - Number of safe reports without Problem Dampener: {result_without_dampener}")

# Part 2: With Problem Dampener
result_with_dampener = count_safe_reports('2.txt', use_dampener=True)
print(f"Part 2 - Number of safe reports with Problem Dampener: {result_with_dampener}")