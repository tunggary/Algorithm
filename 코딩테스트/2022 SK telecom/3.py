def getPlan(planList, clientData:int, clientService:set):
    for i, (planData, planService) in enumerate(planList):
        if clientData <= planData and clientService.issubset(planService):
            return i+1
    return 0

def solution(n, plans, clients):
    answer = []
    planList = []
    service = set()
    for i in range(len(plans)):
        plan = plans[i].split()
        data = int(plan[0])
        service |= set(plan[1:])
        newSet = set(service)
        planList.append([data, newSet])
    planList.sort(key= lambda x : x[0])

    for i in range(len(clients)):
        client = clients[i].split()
        clientData = int(client[0])
        clientService = set(client[1:])
        answer.append(getPlan(planList, clientData, clientService))
        
    return answer
solution(
5, ["100 1 3", "500 4", "2000 5"], ["300 3 5", "1500 1", "100 1 3", "50 1 2"])