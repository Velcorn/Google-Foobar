from itertools import chain, combinations


def solution(l):
    # If sum of elements in list is less than 3, return empty 0
    if sum(l) < 3:
        return 0
    # Get rest when divided by 3
    r = b = sum(l) % 3
    # Loop while rest is not 0
    while b > 0:
        # If rest is in l, remove from l and return l
        if b in l:
            l.remove(b)
            break
        # If rest lte 8, increment b
        elif b <= 8:
            b += 3
        else:
            # Iterate over subsets of two elements of l in ascending order
            for n in combinations(sorted(l), 2):
                # If sum of elements is r, remove them and return l
                if sum(n) == r:
                    l.remove(n[0])
                    l.remove(n[1])
                    b = 0
                    break
            # If removing two not possible, no solution exists
            if b != 0:
                b = 0
                l = []
    # Return list in descending order
    l = sorted(l, reverse=True)
    return "".join(str(x) for x in l) if l else 0


def solution_dumb(l):
    # Dumb solution using superset
    possible_numbers = chain.from_iterable(combinations(l, i) for i in range(len(l)+1))
    biggest_number = 0
    for pn in possible_numbers:
        if not pn:
            continue
        if sum(pn) % 3 == 0:
            number = int(''.join([str(n) for n in sorted(pn, reverse=True)]))
            if number > biggest_number:
                biggest_number = number
    return biggest_number


if __name__ == '__main__':
    print(solution([5, 2]))
    print(solution([3, 1, 4, 1, 1, 1]))
    print(solution([3, 1, 4, 1, 5, 9]))
