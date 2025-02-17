def solution(n):
    s = str(n)
    li = list(s)
    answer = 0
    
    length = len(li)
    
    for num in li:
        answer += int(num)

    return answer