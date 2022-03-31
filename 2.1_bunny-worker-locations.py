def solution(x, y):
    return str((x + y - 1) * (x + y - 2) // 2 + x)


if __name__ == '__main__':
    print(solution(5, 10))
