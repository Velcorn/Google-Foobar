def solution(map):
    # A* using Manhattan distance with 1 optional removal of a wall
    door = (len(map) - 1, len(map[0]) - 1)
    md = door[0] + door[1] + 1
    queue = [[True, md, 1, (0, 0)]]
    visited = set()
    # While queue, if current node is door, return len of path, if node already visited, continue
    # If not, mark as visited, add all possible moves to queue and sort queue by md
    # Optionally remove a wall - single-use
    while queue:
        e = queue.pop(0)
        removal, md, steps, node = e[0], e[1], e[2], e[3]
        if node == door:
            return steps
        if node in visited:
            continue
        visited.add(node)
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = node[0] + dx, node[1] + dy
            if 0 <= nx <= door[0] and 0 <= ny <= door[1]:
                md = door[0] - nx + door[1] - ny + 1
                if map[nx][ny] == 0:
                    queue += [[removal, md, steps + 1, (nx, ny)]]
                elif removal:
                    queue += [[False, md, steps + 1, (nx, ny)]]
        queue = sorted(queue, key=lambda x: x[2])


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
