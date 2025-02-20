def solution(t, p):
    length = len(p) # 부분 문자열 길이
    i = 0
    ss = [] # 부분 문자열
    answer = 0
    
    while i + length <= len(t):
        ss.append(int(t[i:i+length]))
        i += 1
        
    answer = len([s for s in ss if s <= int(p)])
    
    return answer