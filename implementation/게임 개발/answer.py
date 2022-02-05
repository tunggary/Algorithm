#이코테 118p
#아이디어: 방문을 표현해주는 2중 리스트를 리스트 컴프리헨션 문법으로 초기화 해주고, 이동하기 전 조건을 잘 확인해준다.

#input
n,m = map(int, input().split())
x,y,direction = map(int, input().split())
map_info = []
for i in range(n):
  map_info.append(list(map(int, input().split())))

#방문 위치를 확인하기 위한 똑같은 크기의 2중 리스트
check = [[0] * m for _ in range(n)]
check[x][y] = 1

#방문한 좌표의 갯수, 같은 자리에서 회전한 횟수, 죄표평면에서 이동하는 위치를 나타내는 배열
count = 1
turn_count = 0
dx = [-1,0,1,0]
dy = [0,1,0,-1]

#왼쪽으로 90도 회전
def turn_left():
  global direction
  direction -= 1
  if direction == -1:
    direction = 3

#탐색 시작
while True:
  turn_left()
  nx = x + dx[direction]
  ny = y + dy[direction]
  if check[nx][ny] == 0 and map_info[nx][ny] == 0:
    check[nx][ny] = 1
    x = nx
    y = ny
    turn_count = 0
    count += 1
    continue
  else:
    turn_count += 1

  if turn_count == 4:
    nx = x - dx[direction]
    ny = y - dy[direction]
    if map_info[nx][ny] == 0:
      x = nx
      y = ny
      turn_count = 0
    else:
      break

print(count)
