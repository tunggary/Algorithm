n = int(input())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))
  
def find(row, col, n):
  color = graph[row][col]
  for i in range(n):
    for j in range(n):
      if graph[row+i][col+j] != color:
        return False
  return True

result = [0,0]
def dfs(row, col, n):
  if find(row, col, n):
    result[graph[row][col]] += 1
  else:
    half = int(n/2)
    dfs(row, col, half)
    dfs(row, col + half, half)
    dfs(row + half, col, half)
    dfs(row + half, col + half, half)
    
dfs(0,0,n)
print(result[0])
print(result[1])