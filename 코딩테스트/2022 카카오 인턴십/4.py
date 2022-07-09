# answer = []
# def dfs(node, visited, graph, summit, gates, summits, path, maxCost):
#     global answer
#     if node == summit:
#         answer.append((maxCost, summit))
#         return
#     for next, cost in graph[node]:
#         if not visited[next]:
#             if (gates.get(next) == None and summits.get(next) == None) or next == summit:
#                 visited[next] = True
#                 path += str(next)
#                 newMaxCost = max(maxCost, cost)
#                 dfs(next, visited, graph, summit, gates, summits, path, newMaxCost)
#                 path = path[:-1]
#                 visited[next] = False

# def search(gate, summit, graph, n, gates, summits):    
#     dfs(gate, [False]*(n+1), graph ,summit, gates, summits, str(gate), 0)

# def solution(n, paths, gates, summits):
#     global answer
#     graph = [[] for _ in range(n+1)]
#     summits = {summit: summit for summit in summits}
#     gates = {gate: gate for gate in gates}

#     for a,b,w in paths:
#         graph[a].append((b,w))
#         graph[b].append((a,w))

#     for gate in gates.keys():
#         for summit in summits.keys():
#             search(gate, summit, graph, n, gates, summits)
#     answer.sort()
#     return [answer[0][1], answer[0][0]]

from collections import deque
answer_value = int(1e9)
answer_summit = int(1e9)

def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, a,b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a > b:
    parent[a] = b
  else:
    parent[b] = a

def dfs(node, newPaths ,gates, summits, summit, value, visited):
    q = deque([(node,value)])
    global answer_value, answer_summit
    while q:
        now,cost = q.popleft()
        if now == summit:
            if answer_value > cost:
                answer_value = cost
                answer_summit = now
            elif answer_value == cost and answer_summit > now:
                answer_value = cost
                answer_summit = now
            continue
        for next, w in newPaths[now]:
            if not visited[next]:
                if (next not in gates) and ((next not in summits) or (next == summit)):
                    visited[next] = True
                    q.append((next, max(w,cost)))
            
def solution(n, paths, gates, summits):
    paths.sort(key = lambda x: x[2])
    parent = [i for i in range(n+1)]
    newPaths = [[] for _ in range(n+1)]
    for a,b,w in paths:
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            newPaths[a].append((b,w))
            newPaths[b].append((a,w))
    for gate in gates:
        for summit in summits:
            visited = [False]*(n+1)
            visited[gate] = True
            dfs(gate, newPaths, gates, summits, summit, 0, visited)
    return [answer_summit, answer_value]

# solution(7,[[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]],[3, 7],[1, 5])
print(solution(6,[[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]],[1, 3],[5]))