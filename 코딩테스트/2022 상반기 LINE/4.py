#아이디어: 누적합 문제

def solution(arr,brr):
  n = len(arr)
  answer = 0
  
  for i in range(1,n):
    arr[i] += arr[i-1]
    brr[i] += brr[i-1]
  
  for i in range(n):
    if arr[i] != brr[i]:
      answer += 1
  return answer

print(solution([6,2,2,6], [4,4,4,4]))