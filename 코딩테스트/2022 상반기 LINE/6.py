from heapq import heappush, heappop
sell_list = []
buy_list = []
result_info = {}

def buy(buy_price, buy_order, buy_amount, buy_name):
  if len(sell_list) == 0:
    heappush(buy_list, (-buy_price, buy_order, buy_amount, buy_name))
    return
  
  sell_price, sell_order, sell_amount, sell_name = heappop(sell_list)
  if sell_price <= buy_price:
    amount = min(buy_amount,sell_amount)
    price = amount*sell_price
    result_info[buy_name][0] += amount
    result_info[buy_name][1] -= price
    result_info[sell_name][0] -= amount
    result_info[sell_name][1] += price
    
    sell_amount -= amount
    buy_amount -= amount
    if sell_amount > 0:
      heappush(sell_list, (sell_price, sell_order, sell_amount, sell_name))
    if buy_amount > 0:
      buy(buy_price, buy_order, buy_amount, buy_name)
  else:
    heappush(sell_list, (sell_price, sell_order, sell_amount, sell_name))
    heappush(buy_list, (-buy_price, buy_order, buy_amount, buy_name))
      
def sell(sell_price, sell_order, sell_amount, sell_name):
  if len(buy_list) == 0:
    heappush(sell_list, (sell_price, sell_order, sell_amount, sell_name))
    return
  
  buy_price, buy_order, buy_amount, buy_name = heappop(buy_list)
  buy_price = abs(buy_price)
  if sell_price <= buy_price:
    amount = min(buy_amount,sell_amount)
    price = amount*sell_price
    result_info[buy_name][0] += amount
    result_info[buy_name][1] -= price
    result_info[sell_name][0] -= amount
    result_info[sell_name][1] += price
  
    sell_amount -= amount
    buy_amount -= amount
    if buy_amount > 0:
      heappush(buy_list, (-buy_price, buy_order, buy_amount, buy_name))
    if sell_amount > 0:
      sell(sell_price, sell_order, sell_amount, sell_name)
  else:
    heappush(sell_list, (sell_price, sell_order, sell_amount, sell_name))
    heappush(buy_list, (-buy_price, buy_order, buy_amount, buy_name))
  
def solution(req_id, req_info):
  for name in req_id:
    result_info[name] = [0,0]
  
  for i in range(len(req_id)):
    if req_info[i][0] == 0:
      buy(req_info[i][2],i+1,req_info[i][1],req_id[i])
    else:
      sell(req_info[i][2],i+1,req_info[i][1],req_id[i])
      
  answer = []
  for name in list(result_info.keys()):
    string = ""
    string += name + " "
    string +=  '+' + str(result_info[name][0]) if result_info[name][0] > 0 else str(result_info[name][0])
    string += " "
    string +=  '+' + str(result_info[name][1]) if result_info[name][1] > 0 else str(result_info[name][1])
    answer.append(string)
  return answer
    
# solution(["Morgan", "Teo", "Covy", "Covy", "Felix"],[[0, 10, 50], [1, 35, 70], [0, 10, 30], [0, 10, 50], [1, 11, 40]])
print(solution(["William", "Andy", "Rohan", "Rohan", "Louis", "Andy"],[[1, 7, 20], [0, 10, 10], [1, 10, 40], [1, 4, 25], [0, 5, 11], [0, 20, 30]]))