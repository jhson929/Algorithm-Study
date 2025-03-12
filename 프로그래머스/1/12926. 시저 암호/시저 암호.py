# A : 65 / Z : 90
# a : 97 / z : 122
# 공백 : 32

def solution(s, n):  
    s = list(s)
    
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr((ord(s[i]) - ord('A') + n) % 26 + ord('A'))
        elif s[i].islower():
            s[i] = chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))
            
    return "".join(s)