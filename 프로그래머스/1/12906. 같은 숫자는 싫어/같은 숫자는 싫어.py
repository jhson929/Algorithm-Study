def solution(arr):
    answer = []
    x = arr[0]
    answer.append(x) # 첫 숫자 추가
    
    for num in arr[1:]:
        if num == x: # 연속된 숫자일 경우
            continue
        else:
            answer.append(num)
            x = num
    
    return answer