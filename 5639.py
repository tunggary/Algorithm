import sys
sys.setrecursionlimit(1000000)
nodes = []
while True:
  input = sys.stdin.readline()
  if not input:
    break
  nodes.append(int(input))
  
# start = nodes[0]
# tree = {start: [-1,-1]}

# def search(n, node):
#   if node == -1:
#     tree[n] = [-1,-1]
#     return n
#   if node > n:
#     tree[node][0] = search(n,tree[node][0])
#   else:
#     tree[node][1] = search(n,tree[node][1]) 
#   return node

# for i in nodes[1:]:
#   search(i, start)

# def postOrder(n):
#   if n != -1:
#     postOrder(tree[n][0])
#     postOrder(tree[n][1])
#     print(n)

# postOrder(start)

def postOrder(first, last):
  if first > last:
    return 
  mid = last + 1
  for i in range(first+1, last+1):
    if nodes[first] < nodes[i]:
      mid = i
      break
  postOrder(first+1,mid-1)
  postOrder(mid,last)
  print(nodes[first])

postOrder(0, len(nodes)-1)