def solution(arr1, arr2):
    # 코드 최적화
    answer = [[x + y for x, y in zip(a1, a2)] for a1, a2 in zip(arr1, arr2)]
    
    return answer