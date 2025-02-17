def solution(x):
    digits = [int(i) for i in str(x)]
    sum_digits = sum(digits)
    
    return x % sum_digits == 0