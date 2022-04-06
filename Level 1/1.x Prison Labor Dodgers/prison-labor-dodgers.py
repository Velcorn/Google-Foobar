def solution(x, y):
    # Set union - intersection = additional integer
    return next(iter((set(x) | set(y)) - (set(x) & set(y))))


if __name__ == '__main__':
    print(solution([13, 5, 6, 2, 5], [5, 2, 5, 13]))
    print(solution([14, 27, 1, 4, 2, 50, 3, 1], [2, 4, -4, 3, 1, 1, 14, 27, 50]))
