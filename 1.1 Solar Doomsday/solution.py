from math import sqrt


def solution(area):
    # If no area, return empty list
    if area == 0:
        return []
    # Else get the absolute of the square root of the area
    square = int(sqrt(area)) ** 2
    # Return the square + recursive call on the difference
    return [square] + solution(area - square)


if __name__ == "__main__":
    print(solution(12))
