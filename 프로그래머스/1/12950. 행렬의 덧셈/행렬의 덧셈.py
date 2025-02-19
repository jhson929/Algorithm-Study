def solution(arr1, arr2):
    row, col = len(arr1), len(arr1[0])
    answer = []
    for i in range(row): # 행     
        li = []
        for k in range(col):
            li.append(arr1[i][k] + arr2[i][k])
        answer.append(li)
    
    return answer