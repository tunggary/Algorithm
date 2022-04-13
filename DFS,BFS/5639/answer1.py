#백준 5639번
#아이디어: preorder의 순서를 생각해서 왼쪽 자식 노드와 오른쪽 자식 노드 구분하기

import sys
sys.setrecursionlimit(100000)

nodes = []
while True:
  input = sys.stdin.readline()
  if not input:
    break
  nodes.append(int(input))
  
def postOrder(start, end):
  if start > end:
    return
  
  mid = start + 1
  for i in range(start+1, end+1):
    if nodes[i] > nodes[start]:
      mid = i
      break
  
  postOrder(start+1, mid-1)
  postOrder(mid, end)
  print(nodes[start])

postOrder(0,len(nodes)-1)