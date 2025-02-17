def solution(absolutes, signs):
    # 실제 양음 숫자를 담을 리스트 필요
    ls = []
    for i in range(0, len(absolutes)):
        
        if signs[i]:
            ls.append(int(absolutes[i]))
        else:
            ls.append((-1) * int(absolutes[i]))
    
    answer = sum(ls)
    return answer