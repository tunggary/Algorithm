#백준 1541번
#아이디어: -가 나오면 -가 다시 나올때까지 모든 수를 더해서 빼주면 최소값
string = input()

data = string.split("-")
array = []
for i in range(len(data)):
  array.append(sum(map(int,data[i].split("+"))))

result = array[0]
for i in range(1,len(array)):
  result -= array[i]

print(result)