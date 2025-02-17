def solution(n):
    answer = ""
    li = [i for i in str(n)]
    
    li.sort()
    li = li[::-1]
    
    for k in li:
        answer += k
    
    return int(answer)