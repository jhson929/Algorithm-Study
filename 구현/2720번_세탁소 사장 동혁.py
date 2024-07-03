coins = (25, 10, 5, 1) # 달러를 센트로
change = [0, 0, 0, 0]

T = int(input()) # 테스트케이스 입력
for _ in range(T):
    t = int(input()) # 거스름돈 입력
    i = 0
    
    for c in coins:
        change[i] = t // c
        t = t % c
        i += 1
        
    for c in change:
        print(c, end = " ")
    
    print()
    change = [0, 0, 0, 0]
