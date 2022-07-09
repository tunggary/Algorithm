# def solution(stones, k):
#     answer = int(1e9)
#     n = len(stones)
#     for i in range(n-k+1):
#         answer = min(max(stones[i:i+k]), answer)     
#     return answer

def solution(stones, k):
    left = 1
    right = max(stones)
    answer = 0
    while left <= right:
        mid = (left+right)//2
        count = 0
        for stone in stones:
            if stone - mid <= 0:
                count += 1
            else:
                count = 0
            if count >= k:
                break
                
        if count >= k:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
        
    return answer
            

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1],3))