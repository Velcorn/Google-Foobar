def int2base(n, b):
    # Convert an integer n to base b
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(str(int(n % b)))
        n /= b
    return ''.join(digits[::-1])


def solution(n, b):
    # Initialize ids generated so far and keep track of them in a set
    ids = [n]
    unique = set(n)
    while True:
        # Split n into digits, sort them and create x and y from the sorted digits
        digits = sorted([i for i in str(n)])
        x = ''.join(digits)
        y = ''.join(digits[::-1])
        # Subtract x from y and convert the result to base b
        n = int2base(int(y, b) - int(x, b), b).zfill(len(n))
        # If n is '0', return 1
        # Elif check if n has been seen before, then return cycle length
        # Else append/add n to the list/set and continue
        if n == '0':
            return 1
        elif n in unique:
            return len(ids) - ids.index(n)
        else:
            ids.append(n)
            unique.add(n)


if __name__ == '__main__':
    print(solution('1211', 10))
    print(solution('210022', 3))
