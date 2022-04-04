import string


def solution(s):
    abczyx = dict(zip(string.ascii_lowercase, string.ascii_lowercase[::-1]))
    return "".join([abczyx[i] if i in abczyx else i for i in s])


if __name__ == '__main__':
    print(solution("Yyzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"))
