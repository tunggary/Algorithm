from collections import deque

def solution(begin, target, words):
  n = len(words)
  def match(a,b):
    count = 0
    for i in range(len(a)):
      if a[i] != b[i]:
        count += 1
    return count <= 1
  
  def bfs(start):
    q = deque([(start,0)])
    visited = [False]*n
    while q:
      now, count = q.popleft()
      if now == target:
        return count
      for i in range(n):
        if not visited[i] and match(now, words[i]):
          visited[i] = True
          q.append((words[i], count+1))
    return 0
  return bfs(begin)

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))