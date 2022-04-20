from collections import defaultdict

def solution(tickets):
  answer = []
  graph = defaultdict(list)
  for ticket in tickets:
    graph[ticket[0]].append(ticket[1])
  
  for key in graph.keys():
    graph[key].sort()
  print(graph)
  stack = ["ICN"]
  while stack:
    now = stack[-1]
    if not graph[now]:
      answer.append(stack.pop())
    else:
      stack.append(graph[now].pop(0))
  return answer.reverse
    
      
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))