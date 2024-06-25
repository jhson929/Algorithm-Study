N, B = input().split() # B진법 수 N
N = list(N)
B = int(B)
k = 0 # 자릿수
result = 0 # 변환된 값

while N:
    if ord(N[-1]) >= 65:
        result += (ord(N[-1]) - 55) * (B ** k)
    else:
        result += int(N[-1]) * (B ** k)
    
    k += 1
    del N[-1]

print(result)
