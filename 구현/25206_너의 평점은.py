grade = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0,
        'D+':1.5, 'D0':1.0, 'F':0.0}
s = 0 # 학점 * 과목평점 합계
total_class = 0 # 학점의 총합

for _ in range(20):
    ce = input().split()
    
    if ce[2] == 'P':
        continue
    else:
        total_class += float(ce[1])
        s += float(ce[1]) * grade[ce[2]]

print(s / total_class)
