def solution(M, F):
    # Convert input to int
    x, y = int(M), int(F)
    # Initiate counter
    rc = 0
    # While not starting state
    while x > 1 or y > 1:
        # If either x or y is 1, just subtract value of other - 1
        if x == 1:
            rc += y-1
            y -= y-1
        elif y == 1:
            rc += x-1
            x -= x-1
        # Elif either x or y is divisible by the other, it's impossible
        elif x % y == 0 or y % x == 0:
            return 'impossible'
        # Else subtract the largest possible multiple of the smaller number from the larger number
        elif x > y:
            rc += x // y
            x -= y * (x // y)
        else:
            rc += y // x
            y -= x * (y // x)
    # Return counter as string
    return str(rc)


if __name__ == '__main__':
    print(solution('4', '7'))
    print(solution('2', '1'))
    print(solution('2', '4'))
