import math

def solution(s):
    mid = (len(s)-1) / 2
    a, b = math.floor(mid), math.ceil(mid)
    
    if a == b:
        answer = s[a]
    else:
        answer = s[a]+s[b]
        
    return answer