#이코테 332p
#아이디어: 아스키코드값으로 바꿔서 계산

string = input()

result_str = []
result_num = 0

for i in string:
  if ord('1') <= ord(i) <= ord('9'):
    result_num += int(i)
  else:
    result_str.append(i)

result_str.sort()

#list를 str으로 바꾸고, int를 str로 바꿔서 합침
result = ''.join(result_str) + str(result_num)

print(result)
