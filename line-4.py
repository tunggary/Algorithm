# def solution(arr, brr):
#     answer = 0
#     gap = []
#     n = len(arr)
#     for i in range(n):
#       gap.append(brr[i]-arr[i])
    
#     for i in range(n-1):
#       if gap[i] != 0:
#         gap[i+1] += gap[i]
#         gap[i] = 0
#         answer += 1
#     return answer
  

def solution(arr, brr):
    answer = 0
    N = len(arr)
    for idx in range(1,N):
        arr[idx] += arr[idx-1]
        brr[idx] += brr[idx-1]

    for idx in range(N):
        if arr[idx] != brr[idx]:
            answer += 1
    return answer
#누적합
print(solution([3,7,2,4],[4,5,5,2]))
  