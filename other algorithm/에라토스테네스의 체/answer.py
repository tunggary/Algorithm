#이코테: 471p
#아이디어: 특정한 수의 범위안에서 소수를 모두 찾아야할때 사용

n = 1000
array = [True for i in range(n+1)]

for i in range(2, int(n**0.5)+1):
    if array[i] == True:
        j = 2
        while i*j <= n:
            array[i*j] = False
            j += 1
            
for i in range(2, n+1):
    if array[i]:
        print(i, end=" ")
