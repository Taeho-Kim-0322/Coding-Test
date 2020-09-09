######### 예제 4-1 상하좌우
'''
n = int(input())
data = list(input().split())
x, y = 1, 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move = ["L", "R", "U", "D"]


for m in data:
    for i in range(len(move)):
        if m == move[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny


print(nx, ny)
'''



######### 예제 4-2 시각

n = int(input())
count = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                #print(str(i) + str(j) + str(k))
                count += 1

print(count)

