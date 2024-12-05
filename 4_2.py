def read_input(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

def check_mas(s):
    return s in ['MAS', 'SAM']

def find_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    
    def get_diagonal(row, col, dx, dy):
        if not (0 <= row + 2*dx < rows and 0 <= col + 2*dy < cols):
            return ''
        return grid[row][col] + grid[row + dx][col + dy] + grid[row + 2*dx][col + 2*dy]
    
    # For each possible center point of the X
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            # Check both diagonals
            top_left_to_bottom_right = get_diagonal(i-1, j-1, 1, 1)
            top_right_to_bottom_left = get_diagonal(i-1, j+1, 1, -1)
            
            # Check if we have valid MAS patterns (forward or backward) in both diagonals
            if (check_mas(top_left_to_bottom_right) and check_mas(top_right_to_bottom_left)):
                count += 1
    
    return count

def main():
    grid = read_input('4.txt')
    result = find_xmas(grid)
    print(f"Total occurrences of X-MAS: {result}")

if __name__ == "__main__":
    main()