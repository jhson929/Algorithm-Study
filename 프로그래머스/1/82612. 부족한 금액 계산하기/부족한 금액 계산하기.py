def solution(price, money, count):
    answer = -1
    li = [price * i for i in range(1, count+1)]
    
    if money - sum(li) >= 0:
        answer = 0
    else:
        answer = abs(money - sum(li))
        
    return answer