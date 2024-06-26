N, B = map(int, input().split()) # 10진법 수 N, B진법
k = 0 # 자릿수
result = '' # 출력값 

while N: # 몫이 0이 될때까지 반복
    if N % B < 10:
        result = str((N % B)) + result
    else:
        result = chr(N % B + 55) + result
        
    k += 1
    N = N // B
    
print(result)
