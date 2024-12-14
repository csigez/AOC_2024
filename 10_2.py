def read_map(file_path):
    with open(file_path, 'r') as file:
        return [list(map(int, line.strip())) for line in file.readlines()]


def trailhead_ratings(topographic_map):
    rows = len(topographic_map)
    cols = len(topographic_map[0]) if rows > 0 else 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # down, up, right, left
    ratings = []
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    def dfs(x, y):
        if topographic_map[x][y] == 9:
            return 1  # Found a valid trail to height 9
        count = 0

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny]:
                if topographic_map[nx][ny] == topographic_map[x][y] + 1:
                    visited[nx][ny] = True
                    count += dfs(nx, ny)
                    visited[nx][ny] = False

        return count

    for i in range(rows):
        for j in range(cols):
            if topographic_map[i][j] == 0:
                rating = dfs(i, j)
                ratings.append(rating)

    return ratings

# Example usage:
if __name__ == '__main__':
    hiking_map = read_map('10.txt')
    ratings = trailhead_ratings(hiking_map)
    rating = 0
    for r in ratings:
        rating += r
    print(rating)