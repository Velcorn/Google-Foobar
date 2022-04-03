def solution(map):
    # Simple BFS with 1 optional removal of a wall
    queue = [[[True], [(0, 0)]]]
    visited = set()
    # While queue, if current node is goal, return len of path, if node already visited, continue
    # If not, add all possible moves to queue, and mark as visited; optionally remove a wall - single-use
    while queue:
        rpath = queue.pop(0)
        path = rpath[1]
        removal = rpath[0]
        x, y = path[-1]
        if (x, y) == (len(map) - 1, len(map[0]) - 1):
            return len(path)-1
        if (x, y) in visited:
            continue
        visited.add((x, y))
        if map[x][y] == 1:
            removal = False
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(map) and 0 <= ny < len(map[0]):
                if map[nx][ny] == 0:
                    queue.append([[True], [path + (nx, ny)]])
                    print (queue)
                if map[nx][ny] == 1 and removal:
                    queue.append([[False], [path + (nx, ny)]])


if __name__ == '__main__':
    print(solution([[0, 1, 1, 0],
                    [0, 0, 0, 1],
                    [1, 1, 0, 0],
                    [1, 1, 1, 0]]))
    print(solution([[0, 0, 0, 0, 0, 0],
                    [1, 1, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 1, 1],
                    [0, 1, 1, 1, 1, 1],
                    [0, 0, 0, 0, 0, 0]]))
    print(solution([[0, 0, 0, 0, 0, 0],
                    [1, 1, 1, 1, 1, 0],
                    [1, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 1],
                    [0, 1, 1, 1, 1, 1],
                    [0, 0, 0, 0, 0, 0]]))
