def func(number):
    count = 0
    for i in range(1, number+1):
        if number % i == 0:
            count += 1
            
    return count % 2 == 0 # 짝수일경우 True

def solution(left, right):
    answer = 0
    for num in range(left, right+1):
        if func(num):
            answer += num
        else:
            answer -= num

    return answer