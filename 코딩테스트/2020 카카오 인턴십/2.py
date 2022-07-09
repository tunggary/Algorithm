from itertools import permutations

def getOperation(expression:str, order:list):
    ret = -1
    value = -1
    for i in range(len(expression)):
        for j in range(len(order)):
            if ret <= j and expression[i] == order[j]:
                ret = j
                value = i
    return value
            

def dfs(expression:str, order:list, sum:int):
    index = getOperation(expression, order)
    if index > 0:
        if expression[index] == '+':
            sum += dfs(expression[:index],order,sum) + dfs(expression[index+1:],order,sum)
        elif expression[index] == '-':
            sum += dfs(expression[:index],order,sum) - dfs(expression[index+1:],order,sum)
        else:
            sum += dfs(expression[:index],order,sum) * dfs(expression[index+1:],order,sum)
        return sum
    else:
        return int(expression)
    
def solution(expression:str):
    answer = 0
    oper = []
    
    if expression.find('*') > 0:
        oper.append('*')
    if expression.find('+') > 0:
        oper.append('+')
    if expression.find('-') > 0:
        oper.append('-')
    
    for operatorOrder in permutations(oper, len(oper)):
        answer = max(abs(dfs(expression, list(operatorOrder),0)),answer)
    return answer