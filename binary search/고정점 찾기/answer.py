#이코테 368p
#아이디어: 이진 탐색

n = int(input())
array = list(map(int, input().split()))

def binary_search(arr, start, end):
    if start > end:
        return -1
    mid = int((start+end)/2)
    if mid == arr[mid]:
        return mid
    if mid < arr[mid]:
        return binary_search(arr, start, mid-1)
    else:
        return binary_search(arr, mid+1, end)

print(binary_search(array, 0, n-1))
