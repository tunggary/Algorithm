#이코테 180p
#아이디어: sort를 사용할때 lambda 활용하기

n = int(input())

array=[]
for i in range(n):
  data = input().split()
  array.append([data[0], int(data[1])])

result = sorted(array, key = lambda student: student[1])
for student in result:
  print(student[0], end=" ")
