def solution(s):    
    answer = []
    
    answer.append(-1) # 첫 번째 값 미리 삽입
    
    for a in range(1, len(s)):
        for b in range(a-1, -1, -1):            
            if s[a] == s[b]:
                answer.append(a-b)
                break
                
            if b == 0:
                answer.append(-1)
                
    return answer