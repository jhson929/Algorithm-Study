N = int(input())
street = map(int, input().split())
answer = 0

milk = [0, 1, 2]

m = 0
for st in street:
    if st == milk[m]:
        answer += 1
        m += 1

        if m > 2:
            m = 0
    else:
        continue
print(answer)