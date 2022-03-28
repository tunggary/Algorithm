# def check(log):
#   if len(log) > 100:
#     return False
#   if "team_name : " not in log or "application_name : " not in log or "error_level : " not in log or "message : " not in log:
#     return False
#   log = log.replace("team_name : ","")
#   log = log.replace("application_name : ","")
#   log = log.replace("error_level : ","")
#   log = log.replace("message : ","")
  
#   whiteSpace = 0
#   for i in log:
#     if i == ' ':
#       whiteSpace += 1
#     elif not i.isalpha():
#       return False
#   if whiteSpace != 3:
#     return False
#   return True

# def solution(logs):
#   answer = 0
#   for log in logs:
#     if not check(log):
#       answer += 1
#   return answer

import re

def solution(logs):
  p = re.compile("^team_name\s:\s[a-zA-Z]+\sapplication_name\s:\s[a-zA-Z]+\serror_level\s:\s[a-zA-Z]+\smessage\s:\s[a-zA-Z]+$")
  answer = 0
  for log in logs:
    m = p.match(log)
    if not m or len(log)>100:
      answer += 1
  return answer

print(solution(["team_name : MyTeam application_name : YourApp error_level : info messag : IndexOutOfRange", "no such file or directory", "team_name : recommend application_name : recommend error_level : info message : RecommendSucces11", "team_name : recommend application_name : recommend error_level : info message : Success!", "   team_name : db application_name : dbtest error_level : info message : test", "team_name     : db application_name : dbtest error_level : info message : test", "team_name : TeamTest application_name : TestApplication error_level : info message : ThereIsNoError"]))
