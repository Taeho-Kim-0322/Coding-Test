######### 실전 3. 게임 개발


n, m = map(int, input().split())
d = [[0] * m for i in range(n)]

x, y, direction = map(int, input().split())
d[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0
while True:
    #왼쪽 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    #회전 후, 정면에 가보지 않은 칸 & 육지
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        #방문처리
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    #회전 후 정면에 가보았거나 바다인 경우
    else:
        turn_time += 1

    #4번 돌았으나 없으면, 바라보는 방향 유지한 채 한 칸 뒤로 가고 1단계
    if turn_time == 4:
        #뒤로 한 칸
        nx = x - dx[direction]
        ny = y - dy[direction]

        #뒤로갈 수 있으면 이동
        if array[nx][ny] == 0:
            x = nx
            y - ny
            turn_time = 0
        else:
            break
            turn_time = 0


print(count)





#
#
#
#
#
#
# ######### 실전 2. 왕실의 나이트
#
# # n = input()
# # #ord 함수 생각...
# # x , y = int(ord(n[0])) - int(ord('a')) + 1, int(n[1])
# #
# # #갈 수 있는 8가지 방법 다 정해놓고...
# # #8개 다 해보면서 가능하면 cnt +
# # steps = [(-2,-1), (-2, 1), (1, 2), (-1, 2), (2, 1), (2, -1), (-1, -2), (1, -2)]
# # answer = 0
# # for case in steps:
# #     nx = x + case[0]
# #     ny = y + case[1]
# #
# #     if nx < 1 or nx > 8 or ny < 1 or ny > 8:
# #         continue
# #     else:
# #         answer += 1
# #
# # print(answer)
#
#
#
#
#
# ######### 예제 4-1 상하좌우
# '''
# n = int(input())
# data = list(input().split())
# x, y = 1, 1
#
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# move = ["L", "R", "U", "D"]
#
#
# for m in data:
#     for i in range(len(move)):
#         if m == move[i]:
#             nx = x + dx[i]
#             ny = y + dy[i]
#
#     if nx < 1 or ny < 1 or nx > n or ny > n:
#         continue
#     x, y = nx, ny
#
#
# print(nx, ny)
# '''
#
#
#
# ######### 예제 4-2 시각
# '''
# n = int(input())
# count = 0
#
# for i in range(n+1):
#     for j in range(60):
#         for k in range(60):
#             if '3' in str(i) + str(j) + str(k):
#                 #print(str(i) + str(j) + str(k))
#                 count += 1
#
# print(count)
#
# '''