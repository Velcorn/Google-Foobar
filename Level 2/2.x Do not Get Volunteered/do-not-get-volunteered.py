def solution(src, dest):
    # Build chess board
    x, y = 0, 8
    board = []
    for i in range(0, 8):
        board.append([j for j in range(x, y)])
        x, y = y, y + 8
    # BFS with movement of a knight
    visited = set()
    queue = [[0, (src / 8, src % 8)]]
    while queue:
        moves, pos = queue.pop(0)
        if pos in visited:
            continue
        visited.add(pos)
        # Add all possible moves of the knight on the board to the queue
        for dy, dx in [[-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1]]:
            ny, nx = pos[0] + dy, pos[1] + dx
            if 0 <= ny <= 7 and 0 <= nx <= 7:
                if board[ny][nx] == dest:
                    return moves + 1
                queue.append([moves + 1, (ny, nx)])


if __name__ == '__main__':
    print(solution(0, 1))
    print(solution(19, 36))
