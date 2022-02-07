#이코테 137p
#아이디어: 깊이우선탐색은 stack 자료구조를 이용할 수도 있지만, 재귀함수를 이용해 메모리의 스택을 이용할 수 있다.

#인접 행렬
graph = [[],[2,3,8,],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]

visited = [0]*9

def dfs(graph, v, visited):
  visited[v] = True
  print(v, end=" ")
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

dfs(graph, 1, visited)
