def solution(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0: # t가(나머지가) 0이 될때까지
        t = c % d
        c, d = d, t
    answer = [c, int(a*b/c)]
    return answer