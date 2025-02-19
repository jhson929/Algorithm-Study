def solution(s):
    # 조건1 : 문자열 길이
    con1 = False
    if len(s) in [4, 6]:
        con1 = True
    
    # 조건2 : only 숫자
    con2 = True
    try:
        temp = [int(ss) for ss in s]
    except:
        con2 = False

    return con1 and con2