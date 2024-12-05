def read_input(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

def find_XMAS(grid) -> int:
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    
    # All possible directions: right, down-right, down, down-left, left, up-left, up, up-right
    directions = [
        (0, 1), (1, 1), (1, 0), (1, -1),
        (0, -1), (-1, -1), (-1, 0), (-1, 1)
    ]
    
    def check_direction(row, col, dx, dy) -> bool:
        if not (0 <= row + 3*dx < rows and 0 <= col + 3*dy < cols):
            return False
        word = ''
        for i in range(4):
            word += grid[row + i*dx][col + i*dy]
        return word == 'XMAS'
    
    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                if check_direction(i, j, dx, dy):
                    count += 1
    
    return count

def main():
    grid = read_input('4.txt')
    result = find_XMAS(grid)
    print(f"Total occurrences of XMAS: {result}")

if __name__ == "__main__":
    main()