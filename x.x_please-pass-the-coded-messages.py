from itertools import combinations


def helper(l, i):
    rest = sum(l) % 3
    for n in combinations(l, i):
        if sum(n) % 3 == rest:
            l.remove(n[0])
            l.remove(n[1])
            return l
    return helper(l, i+1)


def solution(l):
    if l in [[0], [1], [2]]:
        return 0
    l = sorted(l, reverse=True)
    rest = sum(l) % 3
    while rest != 0:
        if rest in l:
            l.remove(rest)
            break
        elif rest <= 8:
            rest += 3
        else:
            return helper(l, 2)
    return l


if __name__ == '__main__':
    print(solution([3, 1, 4, 1]))
    print(solution([3, 1, 4, 1, 5, 9]))
