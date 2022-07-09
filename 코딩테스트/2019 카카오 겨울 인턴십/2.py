from collections import defaultdict

def solution(s:str):
  s = s[2:-2].split("},{")
  count = defaultdict(int)
  for ele in s:
    for num in ele.split(","):
      count[int(num)] += 1
  print(count)

  return [key for key,_ in sorted(count.items(), key = lambda x : -x[1])]

print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))