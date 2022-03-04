import sys
n,m = map(int, input().split())
data = [int(sys.stdin.readline()) for _ in range(n)]
    
start, end = 1, max(data)

while(start <= end):
    mid = (start + end)//2
    count = 0
    for each in data:
        count += each // mid
        
    if count < m:
        end = mid - 1
    else:
        start = mid + 1
        
print(end)
        