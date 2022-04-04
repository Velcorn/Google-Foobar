def solution(l):
    # Array to keep track of number of divisors for each number
    a = [0] * len(l)
    # Loop through each list index i, then loop through each sublist index j in l[:i],
    # if l[i] is divisible by l[j], increment counter a[i] by 1 and lts counter by a[j]
    lts = 0
    for i in range(len(l)):
        for j in range(i):
            if l[i] % l[j] == 0:
                a[i] += 1
                lts += a[j]
    return lts


if __name__ == '__main__':
    print(solution([1, 1, 1]))
    print(solution([1, 2, 3, 4, 5, 6]))
