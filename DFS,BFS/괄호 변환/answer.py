#이코테 346p
#아이디어: 그대로 구현하면됨, 문제를 꼼꼼히 읽자

def divide(p):
    left = 0
    right = 0
    for i in range(len(p)):
        if p[i] == ')':
            right += 1
        else:
            left += 1
        if left == right:
            return i
def proper(p):
    if p[0] == ')': 
        return False
    count = 0
    for i in p:
        if i == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            return False
    return True
        
def solution(p):
    answer = ''
    if p == '':
        return answer
    if proper(p):
        return p
    
    index = divide(p)
    u = p[:index+1]
    v = p[index+1:]
    
    if proper(u):
        answer = u + solution(v)
    else:
        answer = '(' + solution(v) + ')'
        for i in range(1,len(u)-1):
            if u[i] == ')':
                answer += '('
            else:
                answer += ')'
    return answer
