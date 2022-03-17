#끝나는 시간이 같다면 빨리 시작하는 순서대로 정렬이 되어야 한다.
#예를 들자면
#2
#2 2
#1 2
#의 경우 이 상태로 한다면 (2 2)가 되고 (1 2)는 (2 2)의 끝나는 시간보다 시작시간이 일찍이기 때문에 무시되어 1번의 회의가 진행된다고 나온다. 하지만 정렬을 통해 (1 2)가 먼저 선택되면 (2 2)도 선택이 가능해지기 때문에 가능한 회의는 2번으로 결정된다.
import sys

n = int(sys.stdin.readline())
data = []
for _ in range(n):
  a, b = map(int, sys.stdin.readline().split())
  data.append((a, b))
  
data.sort(key=lambda x : (x[1], x[0]))

last = 0
count = 0
for start, end in data:
  if last <= start:
    count += 1
    last = end
    
print(count)
