#백준 1874번
#아이디어: 수를 차례대로 적절히 스택에 넣고 pop한 원소를 이용해 주어진 수열을 만들 수 있는지 판단

n = int(input())
array = [int(input()) for _ in range(n)]
count = 1
param = True
result = []
stack = []

for i in array:
    while count <= i:
        stack.append(count)
        result.append("+")
        count += 1
    if stack[-1] == i:
        stack.pop()
        result.append("-")
    else:
        print("NO")
        param = False
        break
    
if param:
    for i in result:
        print(i)
    