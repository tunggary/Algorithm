#이코테 327p
#아이디어: 뱀의 위치가 있는 배열을 이용

def turn(current, next):
  if next == 'L':
    ret = (current - 1) % 4
  else:
    ret = (current + 1) % 4
  return ret

n = int(input())
k = int(input())

graph = [[0]*(n+1) for _ in range(n+1)] #맵 정보
snake = [(1,1)] #뱀 있는 곳
info = [] #회전 정보
step = [(0,1),(1,0),(0,-1),(-1,0)] #동 남 서 북

for i in range(k):
  a,b = map(int,input().split())
  graph[a][b] = 1

l = int(input())
for i in range(l):
  a,b = input().split()
  info.append((int(a),b))

row, col = 1, 1 #초기 값
direction = 0 #초기 방향
time = 0 #시간
index = 0 #회전 정보 index
graph[1][1] = 2

while True:
  time += 1
  n_row = row + step[direction][0]
  n_col = col + step[direction][1]

  if 1>n_row or n_row>n or 1>n_col or n_col>n or graph[n_row][n_col] == 2:
    break

  if graph[n_row][n_col] == 1:
    graph[n_row][n_col] = 2
    snake.append((n_row,n_col))
  else:
    graph[n_row][n_col] = 2
    snake.append((n_row,n_col))
    p_row, p_col = snake.pop(0)
    graph[p_row][p_col] = 0

  row, col = n_row, n_col

  if index < l and time == info[index][0]:
    direction = turn(direction, info[index][1])
    index += 1

print(time)
