import re

def solution(logs):
  p = re.compile("^team_name\s:\s[a-zA-Z]+\sapplication_name\s:\s[a-zA-Z]+\serror_level\s:\s[a-zA-Z]+\smessage\s:\s[a-zA-Z]+$")
  answer = 0
  for log in logs:
    m = p.match(log)
    if not m or len(log)>100:
      answer += 1
  return answer