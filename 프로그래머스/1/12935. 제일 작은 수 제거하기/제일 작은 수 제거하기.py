def solution(arr):
    if len(arr) <= 1:
        return [-1]
    
    min_value = arr[arr.index(min(arr))]
    arr.remove(min_value)
    
    return arr