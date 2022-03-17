string = input()

data = string.split("-")
array = []
for i in range(len(data)):
  array.append(sum(map(int,data[i].split("+"))))

result = array[0]
for i in range(1,len(array)):
  result -= array[i]

print(result)