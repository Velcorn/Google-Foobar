from itertools import combinations


def solution(l):
    # If sum of elements in list is less than 3, return empty 0
    if sum(l) < 3:
        return 0
    # Get rest when divided by 3
    r = b = sum(l) % 3
    # Loop while rest is not 0
    while b != 0:
        # If rest is 1, remove rest from list and return list
        if b in l:
            l.remove(b)
            break
        # If rest lte 8, increment b
        elif b <= 8:
            b += 3
        # Else determine two elements in list that sum to rest
        else:
            # Get sublist of l only containing elements less than r
            sl = [i < r for i in l]
            # Test combinations of two elements of sublist
            for n in combinations(sl, 2):
                # If sum of elements in combination equals r, remove elements from list and return list
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
