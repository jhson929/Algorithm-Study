# A : 65 / Z : 90
# a : 97 / z : 122
# 공백 : 32

def solution(s, n):  
    answer = ""
    i = 0
    
    while i < len(s):
        if s[i] == " ":
            answer += " "
            i += 1
            continue
            
        ss = ord(s[i]) + n
        
        # 대소문자 범위
        upper = ord(s[i]) >= 65 and ord(s[i]) <= 90
        lower = ord(s[i]) >= 97 and ord(s[i]) <= 122
        
        if (upper and ss > 90) or (lower and ss > 122):
            ss -= 26
        
        answer += chr(ss)
        i += 1
    
    return answer
            
        