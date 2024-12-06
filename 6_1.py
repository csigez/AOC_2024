def read_map(filename):
    with open(filename, 'r') as f:
        return [list(line.strip()) for line in f.readlines()]

def find_start(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == '^':
                return x, y
    return None

def simulate_guard(grid):
    # Directions: 0=up, 1=right, 2=down, 3=left
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    
    start = find_start(grid)
    if not start:
        return 0
    
    x, y = start
    direction = 0  # Start facing up
    visited = {(x, y)}
    
    while True:
        # Check if next position is within bounds and not an obstacle
        next_x = x + dx[direction]
        next_y = y + dy[direction]
        
        # Check if guard would leave the map
        if (next_x < 0 or next_x >= len(grid[0]) or 
            next_y < 0 or next_y >= len(grid)):
            break
            
        # If there's an obstacle ahead or hitting the boundary, turn right
        if grid[next_y][next_x] == '#':
            direction = (direction + 1) % 4
        else:
            # Move forward
            x, y = next_x, next_y
            visited.add((x, y))
    
    return len(visited)

def main():
    grid = read_map('6.txt')
    result = simulate_guard(grid)
    print(f"The guard will visit {result} distinct positions before leaving the area.")

if __name__ == "__main__":
    main()