#이코테 197p
#아이디어: 매장 내 부품들을 정렬(O(NlogN))하고 M개의 요구제품을 전부 이진탐색으로 찾는다(O(MlogN)) 시간복잡도는 O((M+N)logN)

n = int(input())
array = list(map(int,input().split()))
m = int(input())
data = list(map(int,input().split()))

def binary_search(target, start, end):
  global array
  while start<=end:
    mid = (start+end)//2
    if array[mid] == target:
       return "Yes"
    elif array[mid] < target:
      start = mid + 1
    else:
      end = mid - 1
  return "No"

#O(NlogN)
array.sort()

#O(M)
for i in data:
  #O(logN)
  print(binary_search(i,0,n-1), end=" ")
