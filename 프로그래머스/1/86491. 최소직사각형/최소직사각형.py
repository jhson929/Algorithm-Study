def solution(sizes):
    answer = 0
    w, h = [], []
    
    for s in sizes:
        if s[0] > s[1]:
            s[0], s[1] = s[1], s[0]
        
        w.append(s[0])
        h.append(s[1])
    
    answer = max(w) * max(h)
    
    return answer