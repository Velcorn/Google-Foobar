from itertools import combinations


def helper(l, r, n):
    # Get sublist of l only containing elements less than r
    sl = [i < r for i in l]
    # Test combinations of n elements of sublist
    for n in combinations(sl, n):
        # If sum of elements in combination equals r, remove elements from list and return list
        if sum(n) % 3 == r:
            l.remove(n[0])
            l.remove(n[1])
            return l
    # Else recurse with n + 1
    return helper(l, r, n + 1)


def solution(l):
    # If sum of elements in list is less than 3, return empty 0
    if sum(l) < 3:
        return 0
    # Get rest when divided by 3
    r = b = sum(l) % 3
    # If rest is 0, return l
    if r == 0:
        return l
    # Sort list in descending order
    l = sorted(l, reverse=True)
    # Loop while rest is not 0
    while b != 0:
        # If rest is 1, remove rest from list and return list
        if b in l:
            l.remove(b)
            return l
        # If rest lte 8, increment b
        elif b <= 8:
            b += 3
        # Else call helper to check multiple elements for removal
        else:
            return helper(l, r, 2)


if __name__ == '__main__':
    print(solution([2, 4, 4, 1]))
    print(solution([3, 1, 4, 1]))
    print(solution([3, 1, 4, 1, 5, 9]))
