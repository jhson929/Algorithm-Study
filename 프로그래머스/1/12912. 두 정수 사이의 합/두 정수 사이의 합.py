def solution(a, b):
    answer = 0
    min_n = min(a, b)
    max_n = max(a, b)
    
    if min_n == max_n:
        answer = min_n
    else:   
        for n in range(min_n, max_n+1):
            answer += n
    
    return answer