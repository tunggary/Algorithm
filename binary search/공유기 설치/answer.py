#이코테 369p
#아이디어: 인접한 공유기 사이의 최소 거리를 이진 탐색을 통해 구한다.

n,c = map(int, input().split())
data = []
for _ in range(n):
    data.append(int(input()))

data.sort()

start = 1
end = data[-1] - data[0]
result = 0

while start <= end:
    gap = (start+end)//2
    count = 1
    prevPos = data[0]
    for i in range(1,n):
        if data[i] >= gap + prevPos:
            count += 1
            prevPos = data[i]
    if count >= c:
        start = gap + 1
        result = gap
    else:
        end = gap - 1
print(result)
