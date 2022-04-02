def solution(l):
    # If sum of elements is less than 3, return 0
    if sum(l) < 3:
        return 0
    # Get residue and residue classes of sum of l mod 3
    r = sum(l) % 3
    r1, r2 = {1, 4, 7}, {2, 5, 8}
    # While r is not 0, check if overlap between l and rc, else check other rc, remove min element from l and update r
    while r > 0:
        if r == 1:
            l.remove(min(set(l) & r1)) if set(l) & r1 else l.remove(min(set(l) & r2))
        else:
            l.remove(min(set(l) & r2)) if set(l) & r2 else l.remove(min(set(l) & r1))
        # Update residue
        r = sum(l) % 3
    # Return list as int in descending order
    l = sorted(l, reverse=True)
    return int("".join(str(x) for x in l)) if l else 0


if __name__ == '__main__':
    print(solution([3, 1, 4, 1]))
    print(solution([3, 1, 4, 1, 5, 9]))
