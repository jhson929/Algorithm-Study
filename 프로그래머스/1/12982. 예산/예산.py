def solution(d, budget):
    answer = 0 # 최대 지원 부서 수
    total = 0 # 지원금액 합
    d.sort()
    
    for money in d:
        if total + money > budget:
            break
        total += money
        answer += 1
    
    return answer