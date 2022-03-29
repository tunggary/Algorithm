from heapq import heappop,heappush

def solution(abilities, k):
  
  abilities.sort(reverse=True)
  q = []
  for i in range(0,len(abilities),2):
    if i == len(abilities)-1:
      heappush(q,(-abilities[i],abilities[i],abilities[i]))
      break
    heappush(q,(-(abilities[i]-abilities[i+1]),abilities[i],abilities[i+1]))
  answer = 0
  
  while q:
    now = heappop(q)
    if k > 0:
      answer += now[1]
      k -= 1
    else:
      answer += now[2]
  return answer

print(solution([2, 8, 3, 6, 1, 9, 1, 9], 2))