def solution(arr):
    if len(arr) <= 2:
        return [-1]
    
    min_i = arr.index(min(arr))
    del arr[min_i]
    
    return arr