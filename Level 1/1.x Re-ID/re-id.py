import math


def solution(n):
    string = '23'
    primes = [2, 3]
    i = 5
    while len(string) < 10006:
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
    return string[n:n + 5]


if __name__ == '__main__':
    print(solution(0))
    print(solution(3))
