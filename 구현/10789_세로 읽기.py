max_len = 0
matrix = []
result = ''

for _ in range(5):
    s = input()
    
    if len(s) > max_len:
        max_len = len(s)
        
    matrix.append(list(s))
       
for i in range(5):
    s = matrix[i]
    
    if len(s) < max_len:
        s += ' ' * (max_len - len(s))
    
    matrix[i] = list(s)

for i in range(max_len):
    for n in range(5):
        result += matrix[n][i]

print(result.replace(' ', ''))   
