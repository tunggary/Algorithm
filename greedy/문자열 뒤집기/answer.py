#이코테 313p
#정당성: 1과 0의 연속된 묶음의 갯수가 더 작은 것을 뒤집으면 된다.

string = input()

result = 1

for i in range(1,len(string)):
  if string[i-1] != string[i]: 
    result += 1

print(result//2)
