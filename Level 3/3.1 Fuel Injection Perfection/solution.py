def solution(n):
    # Cast n to int, initiate count
    n = int(n)
    mn = 0
    # With n as binary, if b is even, divide, elif 2 last bits are '01', subtract, else add
    while n > 1:
        b = bin(n)[2:]
        if b[-1] == '0':
            n //= 2
        elif n == 3 or b[-2:] == '01':
            n -= 1
        else:
            n += 1
        # Increment count
        mn += 1
    return mn


if __name__ == "__main__":
    print(solution('4'))
    print(solution('15'))
