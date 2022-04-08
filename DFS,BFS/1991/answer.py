#백준 1991번
#아이디어: preorder, inorder, postorder에 대한 이해

import sys

n = int(sys.stdin.readline())
tree = {}
for _ in range(n):
  parent, left, right = sys.stdin.readline().split()
  tree[parent] = (left, right)
  
result = [[] for _ in range(3)]
def dfs(node):
  if node != '.':
    result[0].append(node)
    dfs(tree[node][0])
    result[1].append(node)
    dfs(tree[node][1])
    result[2].append(node)

dfs('A')
print(''.join(result[0]))
print(''.join(result[1]))
print(''.join(result[2]))
