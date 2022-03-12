def solution(n, clockwise):
  dx = list()
  dy = list()
  
  #시계 방향 이면 동,남,서,북 순서
  if clockwise:
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
  #반시계 방향 이면 남,서,북,동 순서
  else:
    dx = [1,0,-1,0]
    dy = [0,-1,0,1]
  
  #표시할 그래프
  graph = [[0]*n for _ in range(n)]
  
  #4지점에서 출발하는 선들의 포함되는 좌표
  data = [[] for _ in range(4)]
  
  #초기값 (x,y,방향,표시할 숫자)를 저장
  data[0].append((0,0,0,1))
  data[1].append((0,n-1,1,1))
  data[2].append((n-1,n-1,2,1))
  data[3].append((n-1,0,3,1))

  #4지점에서 동시에 출발해서 그래프의 값이 초기값(0)이 아닐때까지 직진, 이미 숫자가 있으면 방향을 변경해서 진행
  flag = True
  while flag:
    for i in range(4):
      x,y, direction, marking = data[i][-1]
      graph[x][y] = marking
      
      #짝수인 경우와 홀수인 경우 중앙에서 끝나는 모양이 다름
      if n % 2 == 0:
        if (n//2)-1<=x<=n//2 and (n//2)-1<=y<=n//2 and i == 3:
          flag = False
          break
      else:
        if x == n//2 and y == n//2:
          flag = False
          break
     
      nx = x + dx[direction]
      ny = y + dy[direction]
      if graph[nx][ny] == 0:
        data[i].append((nx,ny,direction, marking+1))
      else:
        data[i].append((x,y,turn(direction, clockwise), marking))
  
  return graph

#회전을 시켜주는 함수
def turn(direction, clockwise):
  if clockwise:
    return (direction+1)%4
  else:
    return (direction-1)%4
