#이코테 311p
#정당성 : 최대 그룹을 만들어야 하고, 그룹에 포함안되는 사람도 있을 수 있음으로 오름차순 정렬 후 앞에서 부터 그룹을 만들어도 된다.

n = int(input())
data = list(map(int, input().split()))

data.sort()

result = 0 #총 그룹의 수
count = 0 #현재 그룹에 포함된 모험가의 수

for i in data:
  count += 1
  if count >= i:
    result += 1
    count = 0
    
print(result)
