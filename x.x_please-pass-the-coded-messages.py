def remove_elements(l, e1, e2):
    l.remove(e1)
    l.remove(e2)
    return l


def solution(l):
    # If sum of elements in list is less than 3, return empty 0
    if sum(l) < 3:
        return 0
    # Get rest and residual classes of mod 3
    r = sum(l) % 3
    # If sum of elements in list is already divisible by 3, pass
    if r == 0:
        pass
    # Elif any residual class is in l, simply remove it
    elif any(rc in l for rc in [r, r+3, r+6]):
        for rc in [r, r+3, r+6]:
            try:
                l.remove(rc)
            except ValueError:
                pass
    # Else check residual classes and remove the smallest combination of two elements
    else:
        if r == 1:
            if l.count(2) >= 2:
                l = remove_elements(l, 2, 2)
            elif 2 in l and 5 in l:
                l = remove_elements(l, 2, 5)
            elif l.count(5) >= 2:
                l = remove_elements(l, 5, 5)
            else:
                l = remove_elements(l, 8, 8)
        elif r == 2:
            if l.count(1) >= 2:
                l = remove_elements(l, 1, 1)
            elif 1 in l and 7 in l:
                l = remove_elements(l, 1, 7)
            elif l.count(4) >= 2:
                l = remove_elements(l, 4, 4)
            else:
                l = remove_elements(l, 7, 7)
        elif r == 5:
            l = remove_elements(l, 1, 4)
        elif r == 7:
            l = remove_elements(l, 2, 5)
        else:
            if 1 in l and 7 in l:
                l = remove_elements(l, 1, 7)
            else:
                l = remove_elements(l, 4, 4)
    # Return list as int in descending order
    l = sorted(l, reverse=True)
    return int("".join(str(x) for x in l)) if l else 0


if __name__ == '__main__':
    print(solution([5, 5]))
    print(solution([9, 5, 2]))
    print(solution([3, 1, 4, 1]))
    print(solution([3, 1, 4, 1, 5, 9]))
