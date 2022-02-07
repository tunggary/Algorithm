#이코테 143p
#아이디어: 파이썬으로 큐를 구현할 때는 collections 모듈에서 제공하는 deque 자료구조를 활용한다. deque는 스택과 큐의 장점을 모두 채택한 것인데 데이터를 넣고 빼는 속도가 리스트 자료형에 비해 효율적이다.

from collections import deque

graph = [[],[2,3,8,],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]

visited = [0]*9

def bfs(graph, start, visited):
  visited[start] = True
  print(start, end=" ")

  queue = deque([start])

  while queue:
    v = queue.popleft()
    print(v, end=" ")
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True
  
bfs(graph, 1, visited)
