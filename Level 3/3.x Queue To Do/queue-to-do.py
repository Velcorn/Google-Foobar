def solution(start, length):
    # Initialize empty queue and save input length to var for while loop
    queue = []
    i = length
    while i > 0:
        # Add elements from start to start + i to queue
        queue += [x for x in range(start, start + i)]
        # Increment start by input length and decrement loop var
        start += length
        i -= 1
    # Apply xor on the final queue
    return reduce(lambda x, y: x ^ y, queue)


if __name__ == '__main__':
    print(solution(0, 3))
    print(solution(17, 4))
