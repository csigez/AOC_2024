def evaluate_expression(numbers, operators):
    """Evaluate an expression left-to-right with given numbers and operators."""
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += numbers[i + 1]
        elif op == '*':
            result *= numbers[i + 1]
        else:  # op == '||'
            # Convert both numbers to strings, concatenate, then back to int
            result = int(str(result) + str(numbers[i + 1]))
    return result

def solve_part1(input_data):
    """
    Part 1: Only using + and * operators
    Returns the sum of test values from valid equations
    """
    total = 0
    for line in input_data.strip().split('\n'):
        if not line:
            continue
        
        # Parse the line
        test_part, numbers_part = line.split(':')
        test_value = int(test_part)
        numbers = [int(x) for x in numbers_part.strip().split()]
        
        # For n numbers, we need n-1 operators
        num_operators_needed = len(numbers) - 1
        if num_operators_needed == 0:
            continue
        
        # Try all combinations of + and *
        from itertools import product
        found = False
        for ops in product(['+', '*'], repeat=num_operators_needed):
            if evaluate_expression(numbers, ops) == test_value:
                total += test_value
                found = True
                break
                
    return total

def solve_part2(input_data):
    """
    Part 2: Using +, *, and || operators
    Returns the sum of test values from valid equations
    """
    total = 0
    for line in input_data.strip().split('\n'):
        if not line:
            continue
        
        # Parse the line
        test_part, numbers_part = line.split(':')
        test_value = int(test_part)
        numbers = [int(x) for x in numbers_part.strip().split()]
        
        # For n numbers, we need n-1 operators
        num_operators_needed = len(numbers) - 1
        if num_operators_needed == 0:
            continue
        
        # Try all combinations of +, *, and ||
        from itertools import product
        found = False
        for ops in product(['+', '*', '||'], repeat=num_operators_needed):
            if evaluate_expression(numbers, ops) == test_value:
                total += test_value
                found = True
                break
                
    return total

def main():
    # Read and solve actual input
    with open('7.txt', 'r') as f:
        input_data = f.read()
    print("\nPart 1 solution:", solve_part1(input_data))
    print("Part 2 solution:", solve_part2(input_data))

if __name__ == "__main__":
    main()
