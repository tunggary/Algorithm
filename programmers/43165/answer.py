import sys
sys.setrecursionlimit(100000)
# result = 0
# def dfs(arr,layer,value, target):
#   global result
#   n = len(arr)
#   if layer == n:
#     if value == target:
#       result +=1
#       return
#   else:
#     dfs(arr,layer+1,value+arr[layer],target)
#     dfs(arr,layer+1,value-arr[layer],target)

# def solution(numbers, target):
#   global result
#   answer = 0
#   dfs(numbers,0,0,target)
#   return result

def solution(numbers, target):
  if not numbers and target == 0:
    return 1
  elif not numbers:
    return 0
  else:
    return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0]) 
print(solution([1, 1, 1, 1, 1],3))