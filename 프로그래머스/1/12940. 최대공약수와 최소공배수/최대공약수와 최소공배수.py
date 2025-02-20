def solution(a, b):
    answer = []
    if a > b:
        a, b = b, a # a < b임을 보장
    
    # 최대공약수
    x = 1
    for i in range(1, a+1):
        if a % i == 0 and b % i == 0:
            x = i
    answer.append(x)
    
    # 최소공배수
    y = x * (a // x) * (b // x)
    answer.append(y)
    
    return answer