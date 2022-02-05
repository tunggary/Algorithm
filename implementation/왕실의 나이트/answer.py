#이코테 115p
#아이디어: 문자를 아스키코드로 변환해서 사용, 좌표평면에서 나이트가 갈 수 있는 방향을 배열로 표현.

input_xy = input()

#ord() : 아스키코드 값으로 바꿔주는 내장함수
x = int(input_xy[1])
y = int(ord(input_xy[0])) - int(ord('a')) + 1

count = 0
steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

for step in steps:
  nx = x + step[0]
  ny = y + step[1]
  if 1<=nx<=8 and 1<=ny<=8:
    count += 1

print(count)
