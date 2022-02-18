#이코테 296p
#위상정렬: 사이클이 없는 방향 그래프를 방향성에 거스르지 않도록 정렬, 선수 과목이 있는 과목들의 학습 순서를 정할 때 사용

from collections import deque
import sys

v,e = map(int, input().split())
graph = [[] for _ in range(v+1)]
indegree = [0]*(v+1)

for _ in range(e):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    q = deque()
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        print(now, end=" ")
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

topology_sort()
