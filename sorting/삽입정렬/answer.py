#이코테 161p
#삽입정렬: 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입

arr = [5,6,3,7,4,2,1]

for i in range(1, len(arr)):
  for j in range(i, 0, -1):
    if arr[j] < arr[j-1]:
      arr[j], arr[j-1] = arr[j-1], arr[j]
    else:
      break

print(arr)
