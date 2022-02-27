#이코테 381p
#아이디어: 2,3,5의 갯수를 하나씩 늘려가면서 찾기
n = int(input())

i2 = i3 = i5 = 1
value2, value3, value5 = 2, 3, 5
result = 0

for i in range(1, n):
    result = min(value2, value3, value5)
    if result == value2:
        i2 += 1
        value2 = i2 * 2
    if result == value3:
        i3 += 1
        value3 = i3 * 3
    if result == value5:
        i5 += 1
        value5 = i5 * 5
    
print(result)
