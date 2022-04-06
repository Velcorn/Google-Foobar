def solution(s):
    length = len(s)
    # Iterate over possible sequence length
    for i in range(1, length + 1):
        # Count occurrences of sequence of length i
        count = s.count(s[:i])
        # If sequence count * sequence length is equal to string length, we have the result
        if count * i == length:
            return count


if __name__ == '__main__':
    print(solution('abcabcabcabc'))
    print(solution('abccbaabccba'))
