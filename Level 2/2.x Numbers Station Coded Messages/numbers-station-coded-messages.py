def solution(l, t):
    # If sum of entire list is less than target, return [-1, -1]
    if sum(l) < t:
        return [-1, -1]
    # Iterate over subsets of list, return first start and end index of subset that sums to target
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if sum(l[i:j]) == t:
                return [i, j-1]
    return [-1, -1]


if __name__ == '__main__':
    print(solution([4, 3, 10, 2, 8], 12))
    print(solution([1, 2, 3, 4], 15))
