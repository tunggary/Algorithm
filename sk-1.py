#dp를 이용한 풀이 테케는 돌아감
def solution(money, costs):
  n = len(costs)
  
  #동전 단위
  unit = [1,5,10,50,100,500]
  
  #money만큼 만드는데 드는 최소 생산 단가를 저장하는 리스트
  dp = [0]*(money+1)
  dp[1] = costs[0]
  
  #2원부터 구해야하는 money까지 바텀업 방식으로 최소 생산 단가 구함
  for price in range(2, money+1):
    min_value = int(1e9)
    
    #모든 단위별로 price를 구성할 수 있는지 확인하고, 그 중 최소 생산 단가를 구해서 저장
    for i in range(n):
      #price보다 단위가 크면 구성할 수 없음
      if price < unit[i]:
        break 
      min_value = min(min_value, costs[i] + dp[price - unit[i]])
    dp[price] = min_value

  return dp[money]
      
#커뮤니티 피셜 정답 : 항상 큰 단위가 작은 단위의 배수 이므로 
#생산단가 당 단위가 높은 것 부터 차례대로 money를 구성하면 됨(그리디)
def solution2(money, costs):
  n = len(costs)
  
  #동전 단위
  unit = [1,5,10,50,100,500]
  
  #(생산단가 당 단위, 단위, 생산 단가)를 원소로 가지는 리스트
  data = []
  for i in range(n):
    data.append((unit[i]/costs[i], unit[i], costs[i]))
    
  #생산단가 당 단위가 높은 것부터 처리할 수 있도록 정렬
  data.sort(reverse=True)
  
  index = 0
  answer = 0
  while money > 0:
    #money보다 단위가 높은 경우 다음 단위로 넘어감
    if money < data[index][1]:
      index += 1
    #money에서 해당 단위를 빼고, answer에 생산단가를 더해줌
    else:
      money -= data[index][1]
      answer += data[index][2]  
  return answer
  