from collections import deque


def neighbors(x, y):
    return [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]


def is_valid(x, y, N, M):
    return 0 <= x < N and 0 <= y < M


def shortest_path(N, M, x1, y1, x2, y2, maze):
    if maze[x2][y2] == 1:
        return 0

    visited = [[False] * M for _ in range(N)]
    queue = deque([(x1, y1, 0)])

    while queue:
        x, y, distance = queue.popleft()
        visited[x][y] = True

        if x == x2 and y == y2:
            return distance

        for nx, ny in neighbors(x, y):
            if is_valid(nx, ny, N, M) and not visited[nx][ny] and maze[nx][ny] == 0:
                queue.append((nx, ny, distance + 1))

    return 0


N, M = map(int, input().split())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

maze = [list(map(int, input().split())) for _ in range(N)]

result = shortest_path(N, M, x1, y1, x2, y2, maze)
print(result)
