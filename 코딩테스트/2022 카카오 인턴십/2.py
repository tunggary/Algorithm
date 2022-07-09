from collections import deque

def solution(queue1, queue2):
    answer = 0
    n = len(queue1)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    total_sum = sum1 + sum2 
    target = total_sum // 2
        
    while answer <= 2*n:
        if sum1 == target and sum2 == target:
            break
        if sum1 < sum2:
            value = queue2.popleft()
            queue1.append(value)
            sum1 += value
            sum2 -= value
        elif sum1 > sum2:
            value = queue1.popleft()
            queue2.append(value)
            sum1 -= value
            sum2 += value
        answer += 1
    if answer >= 2*n:
        return -1
    else:
        return answer

