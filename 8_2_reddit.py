def uniqueLocationsInBounds() -> int:
    with open("./8.txt") as file:
        con = file.read()
    grid = con.strip().split("\n")
    width, height = len(grid[0]), len(grid)
    antennas = {}

    # Find all antennas with the same frequency (a-z, A-Z, 0-9)
    for y in range(height):
        for x in range(width):
            if grid[y][x] != ".":
                frequency = grid[y][x]
                if frequency not in antennas:
                    antennas[frequency] = []
                antennas[frequency].append({"x": x, "y": y})

    # Count all unique antiNodes from each pair of antennas
    antiNodes = set()
    for frequency, positions in antennas.items():
        for i in range(len(positions)):
            for j in range(len(positions)):
                if i == j:
                    continue

                dx = positions[j]["x"] - positions[i]["x"]
                dy = positions[j]["y"] - positions[i]["y"]

                # Try all positions in the back of a pair of antennas
                for k in range(-50, 51):
                    antinode_x = positions[i]["x"] + dx * k
                    antinode_y = positions[i]["y"] + dy * k

                    # Do bounds checking
                    if 0 <= antinode_x < width and 0 <= antinode_y < height:
                        antiNodes.add(f"{antinode_x},{antinode_y}")
    print(len(antiNodes))

    return len(antiNodes)

antinodes = uniqueLocationsInBounds()
print(antinodes)