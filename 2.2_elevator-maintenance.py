def solution(l):
    # Good luck!
    return [('.'.join(str(i) for i in il)) for il in sorted([[int(i) for i in il] for il in [e.split(".") for e in l]])]


if __name__ == '__main__':
    print(solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]))
    print(solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]))
