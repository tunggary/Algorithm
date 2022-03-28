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
    if k > 0:
      answer += heappop(q)[1]
      k -= 1
    else:
      answer += heappop(q)[2]
  return answer

solution([7, 6, 8, 9, 10],1)