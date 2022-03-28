def solution(num_teams, remote_tasks, office_tasks, employees):
  teams = [[] for _ in range(num_teams+1)]
  min_num = [int(1e9)]*(num_teams+1)
  for i in range(len(employees)):
    info = employees[i].split()
    team = int(info[0])
    tasks = set(info[1:])
    home = True
    if tasks.intersection(set(office_tasks)):
      home = False
    min_num[team] = min(i+1,min_num[team])
    teams[team].append((i+1,home))
  answer = []
  for i in range(1,num_teams+1):
    flag = True
    for employee, house in teams[i]:
      if house:
        answer.append(employee)
      else:
        flag = False
    if flag:
      answer.remove(min_num[i])
  return answer
  
print(solution(3,["development","marketing","hometask"],["recruitment","education","officetask"],["1 development hometask","1 recruitment marketing","2 hometask","2 development marketing hometask","3 marketing","3 officetask","3 development"]))