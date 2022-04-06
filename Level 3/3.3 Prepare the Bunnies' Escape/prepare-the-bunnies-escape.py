def solution(map):
    # A* using Manhattan distance with 1 optional removal of a wall
    door = (len(map) - 1, len(map[0]) - 1)
    visited = set()
    queue = [[True, 1, (0, 0)]]
    # While queue, if neighbor node is door, return steps + 1, if node (under removal state) already visited, continue
    # Else mark as visited, add all possible moves to queue and sort queue by (- removal + steps + Manhattan distance)
    while queue:
        e = queue.pop(0)
        removal, steps, node = e[0], e[1], e[2]
        y, x = node
        if (removal, node) in visited:
            continue
        visited.add((removal, node))
        for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ny, nx = y + dy, x + dx
            if 0 <= nx <= door[1] and 0 <= ny <= door[0]:
                if (ny, nx) == door:
                    return steps + 1
                elif map[ny][nx] == 0:
                    queue.append([removal, steps + 1, (ny, nx)])
                elif removal:
                    queue.append([False, steps + 1, (ny, nx)])
        queue = sorted(queue, key=lambda x: -x[0] + x[1] + door[0] - x[2][0] + door[1] - x[2][1])


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
