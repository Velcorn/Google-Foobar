def int2base(n, b):
    """
    Convert an integer n to base b as a string
    :param n: integer to convert
    :param b: base to convert to
    :return: a string representation of n in base b
    """
    if n == 0:
        return '0'
    string = ''
    while n:
        string += str(int(n % b))
        n /= b
    return string[::-1]


def solution(n, b):
    # Keep track of different IDs both in a set and a list
    unique, ids = set(n), [n]
    while True:
        # Split n into digits, sort them and create x and y from the sorted digits
        digits = sorted([i for i in str(n)])
        x = ''.join(digits)
        y = ''.join(digits[::-1])
        # Subtract x from y and convert the result to base b, fill the missing zeros with '0'
        n = int2base(int(y, b) - int(x, b), b).zfill(len(n))
        # If n is '0', return 1
        # Elif check if n has been seen before, then return cycle length
        # Else append/add n to the list/set and continue
        if n == '0':
            return 1
        elif n in unique:
            return len(ids) - ids.index(n)
        else:
            unique.add(n)
            ids.append(n)


if __name__ == '__main__':
    print(solution('1211', 10))
    print(solution('210022', 3))
