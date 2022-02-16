#이코테 321p

string = input()
sum = 0
half = len(string)//2

for i in range(half):
  sum += int(string[i])
  sum -= int(string[i+half])

if sum == 0:
  print("LUCKY")
else:
  print("READY")
