def solution(data, n):
    # Count occurrences of each number in data using dictionary
    counts = {}
    for d in data:
        if d in counts:
            counts[d] += 1
        else:
            counts[d] = 1
    # Return list of numbers with count lte n
    return [d for d in data if counts[d] <= n]


if __name__ == '__main__':
    print(solution([1, 2, 3], 0))
    print(solution([1, 2, 2, 3, 3, 3, 4, 5, 5], 1))
