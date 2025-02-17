def solution(n):
    li = [x for x in range(1, n+1) if n % x == 1]
    answer = min(li)
    return answer