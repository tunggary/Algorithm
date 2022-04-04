import sys

n = int(sys.stdin.readline())
c = list(map(int, sys.stdin.readline().split()))
sale = [[] for _ in range(n)]
buy = [False]*n
result = 0

for i in range(n):
  m = int(sys.stdin.readline())
  for _ in range(m):
    target, discount = map(int, sys.stdin.readline().split())
    sale[i].append((target, discount))
    
def find_next():
  min_value = int(1e9)
  min_index = 0
  for i in range(n):
    if buy[i]:
      continue
    sum = 0
    for j in range(len(sale[i])):
      if buy[sale[i][j][0]-1]:
        continue
      sum += sale[i][j][1] if c[sale[i][j][0]-1] > sale[i][j][1] else c[sale[i][j][0]-1] - 1
    if min_value >  c[i]-sum:
      min_value = c[i]-sum
      min_index = i
    elif min_value == c[i] - sum:
      if c[min_index] > c[i]:
        min_index = i
  return min_value, min_index

while True:
  min_value, min_index = find_next()
  if min_value == int(1e9):
      break
  result += c[min_index]
  c[min_index] = 0
  buy[min_index] = True
  for index, discount in sale[min_index]:
    if c[index-1] == 0:
      continue
    elif c[index-1] <= discount:
      c[index-1] = 1
    else:
      c[index-1] -= discount
print(result)

# 10 15 20 25 / min(10 - (10 + 14), 15 - (0), 20 - (10), 25 - (9) )
# 0
# [[(3,10),(2,20)],[],[(4,10)],[(1,10)]]
# [False, False, False, False]

# 0 1 10 25 / min(1 - (0), 10 - (10), 25 - (x: 0))
# 10
# [[(3,10),(2,20)],[],[(4,10)],[(1,10)]]
# [True, False, False, False]

# 0 1 0 15 / min(1 - (0), 15 - (x:0))
# 20
# [[(3,10),(2,20)],[],[(4,10)],[(1,10)]]
# [True, False, True, False]

# 0 0 0 15 / min(15-(x:0))
# 21
# [[(3,10),(2,20)],[],[(4,10)],[(1,10)]]
# [True, True, True, False]

# 0 0 0 0 
# 36
# [[(3,10),(2,20)],[],[(4,10)],[(1,10)]]
# [True, True, True, True]