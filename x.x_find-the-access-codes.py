from itertools import combinations


def solution(l):
    lts = set()
    for c in combinations(l, 3):
        if c[2] % c[1] == 0 and c[1] % c[0] == 0:
            lts.add(c)
    return len(lts)


if __name__ == '__main__':
    print(solution([1, 1, 1]))
    print(solution([1, 2, 3, 4, 5, 6]))
