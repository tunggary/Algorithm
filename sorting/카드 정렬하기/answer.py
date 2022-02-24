#이코테 363p
#아이디어: heap을 이용하여 가장 카드 갯수가 작은 카드 묶음을 2개 선택

import heapq
n = int(input())
heap = []
result = 0

for _ in range(n):
    heapq.heappush(heap, int(input()))

while len(heap) != 1:
    first = heapq.heappop(heap)
    second = heapq.heappop(heap)
    sum = first + second
    result += sum
    heapq.heappush(heap, sum)

print(result)
