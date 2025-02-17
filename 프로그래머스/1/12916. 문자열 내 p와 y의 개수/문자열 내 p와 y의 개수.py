def solution(s):
    s = s.lower()
    p, y = s.count('p'), s.count('y')

    return p == y