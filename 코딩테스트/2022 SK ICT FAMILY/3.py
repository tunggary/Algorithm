from math import factorial

def number_of_cases(x1,y1,x2,y2):
  return int(factorial((x2-x1)+(y2-y1)) / (factorial(x2-x1)*factorial(y2-y1)))

def solution(width, height, diagonals):
  answer = 0
  for x,y in diagonals:
    answer += number_of_cases(0,0,x,y-1)*number_of_cases(x-1,y,width,height)
    answer += number_of_cases(0,0,x-1,y)*number_of_cases(x,y-1,width,height)
    answer %= 10000019
  return answer    