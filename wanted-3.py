import sys

n = int(sys.stdin.readline())
string = sys.stdin.readline()
store = []
result = 0
for i in range(len(string)):
  if string[i] == "W":
    store.append([0,0])
  if string[i] == "H":
    if store:
      for j in range(len(store)):
        store[j][0] += 1
  if string[i] == "E":
    if store:
      for j in range(len(store)):
        if store[j][0] > 0:
          store[j][1] += 1
        
for count in store:
  if count[0] > 0:
    result += (2**count[1])-count[1]-1
print(result)

# W H EEE
# W H EE