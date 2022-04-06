def solution(s):
    counts = {}
    for i in range(len(s)):
        for j in range(1, len(s) + 1):
            ss = s
            # If sequence is longer than remaining string, wrap around
            if i+j >= len(s):
                ss = s[i:]+s[:len(s)-j]
            # Count occurrences of sequence
            if ss[i:i+j] in counts:
                counts[ss[i:i+j]] += 1
            else:
                counts[ss[i:i+j]] = 1
    print (counts)
    return max([v for k, v in counts.items() if len(s) - len(k) * v == 0])


if __name__ == '__main__':
    print(solution('abcabcabcabc'))
    print(solution('abccbaabccba'))
