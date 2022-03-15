#백준 1676번

n = int(input())

result = 1
for i in range(1,n+1):
  result *= i
  
count = 0
while result % 10 == 0:
  result //= 10
  count += 1

print(count)