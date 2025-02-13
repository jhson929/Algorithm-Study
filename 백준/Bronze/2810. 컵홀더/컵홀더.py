N = int(input()) # 좌석 수
chair = input() # 좌석 정보

chair = chair.replace('LL', 'C')

if "C" in chair:
    print(len(chair) + 1)
else:
    print(len(chair))