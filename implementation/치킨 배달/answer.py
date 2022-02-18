#이코테 332p
#아이디어: 최대 m개를 골라서 그 중 최소값을 구해야하므로, 콤비네이션을 이용해 m개를 고를 수 있는 경우를 모두 고른다

from itertools import combinations

def get_chicken_distance(house, chicken):
  sum = 0
  for h_row, h_col in house:
    distance = int(1e9)
    for c_row, c_col in chicken:
      distance = min(distance, abs(h_row-c_row)+abs(h_col-c_col))
    sum += distance
  return sum

n,m = map(int,input().split())
graph = []
house = []
chicken = []
for _ in range(n):
  graph.append(list(map(int, input().split())))

for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
      house.append((i,j))
    elif graph[i][j] == 2:
      chicken.append((i,j))

comb = list(combinations(chicken, m))

result = int(1e9)
for selected in comb:
  result = min(result, get_chicken_distance(house, selected))

print(result)
