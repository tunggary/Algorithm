def solution(answers):
  answer = []
  n = len(answers)
  count = [0,0,0]
  answer1 = [1,2,3,4,5]
  answer2 = [2,1,2,3,2,4,2,5]
  answer3 = [3,3,1,1,2,2,4,4,5,5]
  for i in range(n):
    if answers[i] == answer1[i%5]:
      count[0] += 1
    if answers[i] == answer2[i%8]:
      count[1] += 1
    if answers[i] == answer3[i%10]:
      count[2] += 1
  
  max_value = 0 
  for i in range(3):
    if count[i] > max_value:
      answer.append(i+1)
      max_value = count[i]
    elif count[i] == max_value:
      answer.append(i+1)
  return answer

print(solution([1,3,2,4,2]))