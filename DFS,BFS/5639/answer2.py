#백준 5639번 변형 postorder를 입력으로 받아 preorder로 출력
#아이디어: postorder의 순서를 생각해서 왼쪽 자식 노드와 오른쪽 자식 노드 구분하기

import sys
sys.setrecursionlimit(100000)

nodes = []
while True:
  input = sys.stdin.readline()
  if not input:
    break
  nodes.append(int(input))
  
def preOrder(start, end):
  if start > end:
    return
  
  mid = start - 1
  for i in range(end-1, start-1, -1):
    if nodes[i] < nodes[end]:
      mid = i
      break
  
  print(nodes[end])
  preOrder(start, mid)
  preOrder(mid+1, end-1)

preOrder(0,len(nodes)-1)