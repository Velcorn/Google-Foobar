from itertools import combinations


def solution(num_buns, num_required):
    keys_per_bunny = num_buns - num_required + 1
    bunnies = [[] for i in range(num_buns)]
    for i, combination in enumerate(combinations(range(num_buns), keys_per_bunny)):
        for bunny in combination:
            bunnies[bunny].append(i)
    return bunnies


if __name__ == "__main__":
    print(solution(2, 1))
    print(solution(4, 4))
    print(solution(5, 3))
