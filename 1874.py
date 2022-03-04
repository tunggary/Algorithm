n = int(input())
param = True
count = 1
stack = []
result = []
for _ in range(n):
    data = int(input())
    while count <= data:
        stack.append(count)
        result.append("+")
        count += 1
        
    if stack[-1] == data:
        stack.pop()
        result.append("-")
    else:
        param = False
        print("NO")
        break
        
if param:
    for i in result:
        print(i)