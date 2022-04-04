def solution(n, b):
    ids = [n]
    while True:
        digits = sorted([i for i in str(n)])
        print(digits)
        x = ''.join(digits)
        y = ''.join(digits[::-1])
        n = str(int(y, b) - int(x, b)).zfill(len(n))
        print(n)
        if n == '0':
            return 1
        if n in ids:
            return len(ids) - ids.index(n)
        else:
            ids.append(n)


if __name__ == '__main__':
    print(solution('1211', 10))
    print(solution('210022', 3))
