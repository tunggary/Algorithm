#이코테 110p
#아이디어: 좌표계에서 이동할 때 dx, dy 처럼 배열에 이동할 값을 두고 현재 좌표에서 더하는 식으로 이동

n = int(input())
plans = input().split()

x, y = 1, 1
step = ['L', 'R', 'U', 'D']
dx = [0,0,-1,1]
dy = [-1,1,0,0]

for plan in plans:
  #step의 index를 통해 dx, dy의 값을 이용할 수 있음으로 for문을 아래와 같이 돌린다.
  for i in range(len(step)):
    if plan == step[i]:
      nx = x + dx[i]
      ny = y + dy[i]

  if nx < 1 or nx > n or ny < 1 or ny > n:
    continue
  x, y = nx, ny

print(nx, ny)   
