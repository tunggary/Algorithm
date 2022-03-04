#백준 1654번
#아이디어: 이분 탐색으로 랜선의 길이를 정한다.

n,k = map(int, input().split())
lan = [int(input()) for _ in range(n)]

end = max(lan)
start = 1

while start <= end:
    mid = (start + end) // 2
    count = 0
    for each in lan:
        count += each // mid
    
    if count < k:
        end = mid - 1
    else:
        start = mid + 1

print(end)
         