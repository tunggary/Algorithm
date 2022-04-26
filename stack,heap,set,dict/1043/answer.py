#백준 1043번
#아이디어: set을 이용해서 풀이, 진실을 아는 사람이 생길때마다 다시 모든 파티 확인

import sys
input = sys.stdin.readline

n,m = map(int, input().split())
peopleKnow = set(list(map(int, input().split()))[1:])
parties = [set(list(map(int, input().split()))[1:]) for _ in range(m)]
possible = [1]*m

for _ in range(m):
    for j in range(m):
      if parties[j] & peopleKnow:
        peopleKnow |= parties[j]
        possible[j] = 0
        
print(sum(possible))