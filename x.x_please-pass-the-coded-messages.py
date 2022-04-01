from itertools import combinations


def helper(l, r, n):
    sl = [i < r for i in l]
    for n in combinations(sl, n):
        if sum(n) % 3 == r:
            l.remove(n[0])
            l.remove(n[1])
            return l
    return helper(l, r, n + 1)


def solution(l):
    if l in [[0], [1], [2]]:
        return 0
    l = sorted(l, reverse=True)
    r = sum(l) % 3
    b = r
    while b != 0:
        if b in l:
            l.remove(b)
            break
        elif b <= 8:
            b += 3
        else:
            return helper(l, r, 2)
    return l


if __name__ == '__main__':
    print(solution([3, 1, 4, 1]))
    print(solution([3, 1, 4, 1, 5, 9]))
