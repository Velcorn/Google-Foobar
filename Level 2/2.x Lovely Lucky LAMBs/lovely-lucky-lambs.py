def solution(total_lambs):
    # If less than 3 lambs, difference between the two options is 0
    if total_lambs < 3:
        return 0
    # Else build lists of lamb distribution for the 2 patterns
    max_hm = [1, 1]
    while True:
        lambs = [max_hm[-1] + max_hm[-2]]
        if sum(max_hm + lambs) > total_lambs:
            break
        max_hm.append(lambs[-1])
    min_hm = [1]
    while True:
        lambs = [min_hm[-1] * 2]
        if sum(min_hm + lambs) > total_lambs:
            break
        min_hm.append(lambs[-1])
    # Simply return the difference between the length of the two lists
    return len(max_hm) - len(min_hm)


if __name__ == '__main__':
    print(solution(143))
    print(solution(10))
