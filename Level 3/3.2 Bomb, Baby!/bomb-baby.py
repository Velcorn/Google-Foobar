def solution(M, F):
    # Convert input to int
    x, y = max(int(M), int(F)), min(int(M), int(F))
    # Initiate counter
    rc = 0
    # While y > 1, subtract y time number y fits into x from x, then y is new x and x mod y is new y
    while y > 1:
        rc += x // y
        x, y = y, x % y
    # If y is 1, just need to subtract y from x x - 1 times
    if y == 1:
        return str(rc + x - 1)
    else:
        return 'impossible'


if __name__ == '__main__':
    print(solution('4', '7'))
    print(solution('2', '1'))
    print(solution('2', '4'))
