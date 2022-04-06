import math


def solution(n):
    # First create string of primes of length >= 10,006
    string = '23'
    primes = [2, 3]
    i = 5
    while len(string) < 10006:
        # A number is prime if its square root is not divisible by any smaller prime
        sqrt = math.sqrt(i)
        pds = []
        for p in primes:
            if p <= sqrt:
                pds.append(p)
            else:
                break
        prime = True
        for pd in pds:
            if sqrt % pd == 0:
                prime = False
                break
        if prime:
            string += str(i)
            primes.append(i)
        i += 2
    # Now we can simply return the string + 5 digits for the given index
    return string[n:n + 5]


if __name__ == '__main__':
    print(solution(0))
    print(solution(3))
