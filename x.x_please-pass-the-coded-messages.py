from itertools import combinations


def solution(l):
    # If sum of elements in list is less than 3, return empty 0
    if sum(l) < 3:
        return 0
    # Get rest when divided by 3
    r = b = sum(l) % 3
    # Loop while rest is not 0
    while b != 0:
        # If rest is in l, remove from l and return l
        if b in l:
            l.remove(b)
            break
        # If rest lte 8, increment b
        elif b <= 8:
            b += 3
        else:
            # Iterate over combinations of two elements of l in ascending order
            for n in combinations(sorted(l), 2):
                # If sum of elements has same r as l, remove them and return l
                if sum(n) % 3 == r:
                    l.remove(n[0])
                    l.remove(n[1])
                    b = 0
                    break
    # Return list in descending order
    return sorted(l, reverse=True)


if __name__ == '__main__':
    print(solution([3, 1, 4, 1]))
    print(solution([3, 1, 4, 1, 5, 9]))
