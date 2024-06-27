# 처음 버전
N, M = map(int, input().split())
matrix1 = []
matrix2 = []
result = []

for _ in range(N):
    n = list(input().split())
    matrix1.append(n)
    
for _ in range(N):
    n = list(input().split())
    matrix2.append(n)

for i in range(N):
    li = []
    for j in range(M):
        li.append(int(matrix1[i][j]) + int(matrix2[i][j]))
    
    result.append(li)
        
for i in range(N):
    for j in range(M):
        print(result[i][j], end=" ")

# 가독성있게 정리한 코드
def make_matrix(rows):
    return [list(map(int, input().split())) for _ in range(rows)]

def add_matrix(m1, m2):
    return [[m1[i][j] + m2[i][j] for j in range(len(m1[0]))]for i in range(len(m1))]
            

N, M = map(int, input().split()) # N*M

matrix1 = make_matrix(N)
matrix2 = make_matrix(N)

result = add_matrix(matrix1, matrix2)
        
for i in range(N):
    for j in range(M):
        print(result[i][j], end=" ")
