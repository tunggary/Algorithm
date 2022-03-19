#백준 18870번
#아이디어: 중복을 제거하고 리스트 내에서 자신보다 작은 원소의 갯수를 구해야함

import sys
n = int(sys.stdin.readline())
data = list(map(int, input().split()))

num = sorted(list(set(data)))
dic = {num[i]:i for i in range(len(num))}
for i in data:
  print(dic[i], end=" ")