def solution(n):
    # 10진법 -> 3진법 + 반전
    answer = 0
    n3_reverse = []
    while n != 0:
        n3_reverse.append(n%3)
        n //= 3
    
    k = len(n3_reverse) - 1
    for nn in n3_reverse:
        answer += nn * (3 ** k)
        k -= 1
        
    return answer