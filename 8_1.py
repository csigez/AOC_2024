def read_grid(filename):
    with open(filename, 'r') as f:
        return [list(line.strip()) for line in f]

def find_antennas(grid):
    # Find all antennas grouped by frequency
    antennas = {}
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            char = grid[y][x]
            if char != '.':
                if char not in antennas:
                    antennas[char] = []
                antennas[char].append((x, y))
    return antennas

def distance(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

def calculate_antinodes(antenna1, antenna2):
    x1, y1 = antenna1
    x2, y2 = antenna2
    
    # Vector from antenna1 to antenna2
    dx = x2 - x1
    dy = y2 - y1
    
    # For each point in the grid, check if it's an antinode
    antinodes = []
    
    # Try extending the line in both directions
    for t in [-1, 1]:  # Try both directions
        # Point that makes antenna1 twice as far as antenna2
        # This point is at distance d from antenna2 in the direction of the line
        x = x2 + t * dx
        y = y2 + t * dy
        
        # Check if this point satisfies our condition
        d1 = distance((x, y), antenna1)
        d2 = distance((x, y), antenna2)
        if abs(d1/d2 - 2.0) < 0.0001:
            antinodes.append((x, y))
        
        # Point that makes antenna2 twice as far as antenna1
        x = x1 - t * dx
        y = y1 - t * dy
        d1 = distance((x, y), antenna1)
        d2 = distance((x, y), antenna2)
        if abs(d2/d1 - 2.0) < 0.0001:
            antinodes.append((x, y))
    
    return antinodes

def is_in_bounds(point, grid):
    x, y = point
    return (0 <= int(round(x)) < len(grid[0])) and (0 <= int(round(y)) < len(grid))

def solve(filename):
    grid = read_grid(filename)
    antennas = find_antennas(grid)
    antinodes = set()
    
    # For each frequency
    for freq, positions in antennas.items():
        # For each pair of antennas with the same frequency
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                # Calculate antinodes for this pair
                new_antinodes = calculate_antinodes(positions[i], positions[j])
                
                # Add antinodes that are in bounds
                for antinode in new_antinodes:
                    if is_in_bounds(antinode, grid):
                        # Round to nearest integer coordinates
                        antinodes.add((int(round(antinode[0])), int(round(antinode[1]))))
    
    return len(antinodes)

if __name__ == "__main__":
    result = solve("8.txt")
    print(f"Number of unique antinode locations: {result}")