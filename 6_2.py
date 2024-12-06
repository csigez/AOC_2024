def read_map(filename):
    with open(filename, 'r') as f:
        return [list(line.strip()) for line in f.readlines()]

def find_start(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == '^':
                return x, y
    return None

def simulate_guard_with_obstacle(grid, obstacle_x, obstacle_y):
    # Make a copy of the grid and place the obstacle
    grid = [row[:] for row in grid]
    grid[obstacle_y][obstacle_x] = '#'
    
    # Directions: 0=up, 1=right, 2=down, 3=left
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    
    start = find_start(grid)
    if not start:
        return None
    
    x, y = start
    direction = 0  # Start facing up
    visited = set()
    path = []
    
    while True:
        state = (x, y, direction)
        if state in visited:
            # Found a loop
            return True
        
        visited.add(state)
        path.append((x, y))
        
        # Check if next position is within bounds and not an obstacle
        next_x = x + dx[direction]
        next_y = y + dy[direction]
        
        # Check if guard would leave the map
        if (next_x < 0 or next_x >= len(grid[0]) or 
            next_y < 0 or next_y >= len(grid)):
            return False
            
        # If there's an obstacle ahead, turn right
        if grid[next_y][next_x] == '#':
            direction = (direction + 1) % 4
        else:
            # Move forward
            x, y = next_x, next_y

def find_loop_positions(grid):
    start_pos = find_start(grid)
    if not start_pos:
        return []
    
    loop_positions = []
    
    # Try each empty position
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            # Skip positions that are already occupied or the start position
            if grid[y][x] != '.' or (x, y) == start_pos:
                continue
            
            # Check if placing an obstacle here creates a loop
            if simulate_guard_with_obstacle(grid, x, y):
                loop_positions.append((x, y))
    
    return loop_positions

def main():
    grid = read_map('6.txt')
    loop_positions = find_loop_positions(grid)
    print(f"There are {len(loop_positions)} positions where placing an obstacle would create a loop.")

if __name__ == "__main__":
    main()