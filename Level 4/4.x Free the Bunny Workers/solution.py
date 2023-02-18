from itertools import combinations


def solution(num_buns, num_required):
    # Calculate the number of keys required per bunny
    keys_per_bunny = num_buns - num_required + 1
    # Initialize empty list of keys
    bunnies = [[] for i in range(num_buns)]
    # Iterate over the enumeration of combinations of keys with range(num_buns) and keys_per_bunny
    for i, combination in enumerate(combinations(range(num_buns), keys_per_bunny)):
        # Iterate over the combination
        for bunny in combination:
            # Append the current combination to the list of keys for the current bunny
            bunnies[bunny] += [i]
    return bunnies


if __name__ == "__main__":
    print(solution(2, 1))
    print(solution(4, 4))
    print(solution(5, 3))
