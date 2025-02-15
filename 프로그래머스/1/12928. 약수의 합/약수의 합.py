def solution(n):
    li = [] # n의 약수들
    
    for i in range(1, n+1):
        if n % i == 0:
            li.append(i)
        
    return sum(li)