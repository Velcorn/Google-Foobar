def solution(s):
    # Iterate over cs in string, if c is '>', iterate over c2s in substring from index of c to end of string,
    # if c2 is '<', increase salutes by 2
    salutes = 0
    for i, c in enumerate(s):
        if c == '>':
            for c2 in s[i:]:
                if c2 == '<':
                    salutes += 2
    return salutes


if __name__ == '__main__':
    print(solution('>----<'))
    print(solution('<<>><'))
