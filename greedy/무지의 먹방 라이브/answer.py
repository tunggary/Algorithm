#이코테 316p
#정당성: 음식 시간이 작은 것 부터 사라짐을 이용하여 음식 시간이 작은 것 부터 처리한다.

import heapq

def solution(food_times, k):
    
    if sum(food_times) <= k:
        return -1
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q,(food_times[i], i+1))
        
    sum_value = 0
    prev = 0
    length = len(food_times)
    
    while sum_value + (q[0][0] - prev)*length <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - prev)*length
        length -= 1
        prev = now
    result = sorted(q, key=lambda x: x[1])
    return result[(k-sum_value)%length][1]
