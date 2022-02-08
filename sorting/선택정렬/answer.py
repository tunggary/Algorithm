#이코테 157p
#선택정렬: 처리되지 않은 데이터 중에서 가장 작은 데이터를 맨 앞에 있는 데이터와 바꾸는 것을 반복

arr = [5,6,3,7,4,2,1]

for i in range(len(arr)):
  min_index = i
  for j in range(i+1, len(arr)):
    if arr[min_index] > arr[j]:
      arr[min_index],arr[j] = arr[j], arr[min_index]

print(arr)
