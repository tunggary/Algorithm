from collections import deque
from datetime import datetime, timedelta 

def dateToIndex(date):
  year = int(date[:4])
  month = int(date[5:7])
  day = int(date[8:10])
  
  index = (year - 2021)*365
  month = ()
    
def solution(masks, dates):
  graph = dict()
  visited = dict()
  for year in range(2021, 2031):
    for month in range(1,13):
      for day in range(1,32):
        if month == 2 and day > 28:
          break
        elif month in [4,6,9,11] and day > 30:
          break
        key = str(year)
        key += '/'
        key += "0"+str(month) if month < 10 else str(month)
        key += '/'
        key += "0"+str(day) if day < 10 else str(day)
        graph[key] = 0
        visited[key] = int(1e9)
        
  first = "2030/12/31"
  for date in dates:
    dateInfo = date.split("~")
    if len(dateInfo) == 1:
      graph[dateInfo[0]] = 1
    else:
      start = datetime.strptime(dateInfo[0], "%Y/%m/%d") 
      last = datetime.strptime(dateInfo[1], "%Y/%m/%d")
      while start <= last: 
        dates = start.strftime("%Y/%m/%d")
        if not (dates[5:7] == "02" and dates[8:10] == '29'):
          graph[dates] = 1
          first = min(first, dates)
        start += timedelta(days=1)
  print(first)
  bfs(first, masks, graph, visited)
  
solution(1, ["2022/05/02", "2022/05/01", "2022/05/07", "2022/05/05", "2022/05/08", "2022/05/13~2022/05/15", "2022/05/14~2022/05/17", "2022/05/01~2022/05/02", "2022/05/16"])
