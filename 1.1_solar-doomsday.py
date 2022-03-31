from math import sqrt


def solution(area):
    if area == 0:
        return []
    square = int(sqrt(area)) ** 2
    return [square] + solution(area - square)


if __name__ == "__main__":
    print(solution(12))
