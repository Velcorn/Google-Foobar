def solution(xs):
    # Filter out zeroes from the list
    non_zero = [i for i in xs if i != 0]
    # Get negative numbers
    negative_numbers = [i for i in non_zero if i < 0]
    # If uneven number of negative numbers, remove the biggest from the non-zero list
    if len(negative_numbers) % 2 != 0:
        non_zero.remove(max(sorted(negative_numbers)))
    # Return the product of the remaining numbers
    return reduce(lambda x, y: x * y, non_zero)


if __name__ == '__main__':
    print(solution([2, 0, 2, 2, 0]))
    print(solution([-2, -3, 4, -5]))
