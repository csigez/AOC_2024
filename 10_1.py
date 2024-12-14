def read_topographic_map(file_path):
    with open(file_path, 'r') as file:
        return [list(map(int, line.strip())) for line in file.readlines()]


def trailhead_scores(topographic_map):
    rows = len(topographic_map)
    cols = len(topographic_map[0]) if rows > 0 else 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # down, up, right, left
    scores = []

    def dfs(x, y, visited):
        if (x, y) in visited:
            return 0
        visited.add((x, y))
        count = 1 if topographic_map[x][y] == 9 else 0

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if topographic_map[nx][ny] == topographic_map[x][y] + 1:
                    count += dfs(nx, ny, visited)

        return count

    for i in range(rows):
        for j in range(cols):
            if topographic_map[i][j] == 0:
                visited = set()
                score = dfs(i, j, visited)
                scores.append(score)

    return scores

# Example usage:
if __name__ == '__main__':
    topographic_map = read_topographic_map('10.txt')
    scores = trailhead_scores(topographic_map)
    score = 0
    for s in scores:
        score += s
    print(score)