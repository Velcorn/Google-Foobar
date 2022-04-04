def solution(map):
    # BFS with 1 optional removal of a wall
    door = (len(map) - 1, len(map[0]) - 1)
    removal = True
    queue = [[removal, [(0, 0)]]]
    visited = set()
    # While queue, if current node is door, return len of path, if node already visited, continue
    # If not, mark as visited, add all possible moves to queue and sort queue by md
    # Optionally remove a wall - single-use
    while queue:
        rp = queue.pop(0)
        removal, path = rp[0], rp[1]
        x, y = path[-1]
        if (x, y) == door:
            return len(path)
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx <= door[0] and 0 <= ny <= door[1]:
                if map[nx][ny] == 0:
                    queue += [[removal, path + [(nx, ny)]]]
                elif removal:
                    queue += [[False, path + [(nx, ny)]]]


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
