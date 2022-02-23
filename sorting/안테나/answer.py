#이코테 360p
#아이디어: 안테나를 가운데 집에 설치해야 모든 집까지의 거리가 최소가 됨

n = int(input())
data = list(map(int, input().split()))

data.sort()
print(data[(n-1)//2])
