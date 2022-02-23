#이코테 359p
#아이디어: 람다함수 이용하여 정렬 조건 정하기

n = int(input())
data = []
for _ in range(n):
    name, kor, eng, math = input().split()
    data.append((int(kor),int(eng),int(math),name))

data.sort(key=lambda x: (-x[0],x[1],-x[2],x[3]))

for info in data:
    print(info[3])
