#백준 18111번
#아이디어: 완전탐색을 하여 전체 결과 중 가장 시간이 적게 드는 경우를 구한다.
import sys

n,m,b = map(int, input().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
result_time = int(1e9)
result_height = 0

for height in range(257):
    dig = 0
    stack = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] < height:
                stack += (height - graph[i][j])
            else:
                dig += (graph[i][j] - height)
                
    if stack > b + dig:
        continue
    time = 2*dig + stack
    if result_time >= time:
        result_time = time
        result_height = height
print(result_time, result_height)