from itertools import combinations

# O(n*m + 2^n*n) n<=15, m<=100,000 따라서 10,000,000이하
def solution(sentences, n):
  require_key_list = []
  
  # 시간복잡도 O(n*m)
  for sentence in sentences:
    #sentence를 구성하는데 필요한 문자 ex) line = ('l','i','n','e') / set()은 집합(중복허용x)으로써 add를 하면 집합내의 중복은 제거된다.
    require_key = set()
    #sentence를 구성했을때 점수 ex) 'line IN' = 1+1+1+1+1+2+2 = 9
    score = 0
    
    #sentence를 구성하는데 필요한 문자와 점수를 구함
    for word in sentence:
      #빈칸일때는 점수 +1
      if word == " ":
        score += 1
      #대문자일때는 소문자와,"shift"를 집합에 넣어줌, 점수 +2
      elif word.isupper():
        require_key.add("shift")
        require_key.add(word.lower())
        score += 2
      #대문자일때는 소문자를 넣어줌, 점수 +1
      else:
        require_key.add(word)
        score += 1
    #sentence를 구성하는데 필요한 문자와 점수를 저장
    require_key_list.append((require_key, score))
    
  answer = 0
  #시간 복잡도(2^n*n)
  #require_key_list중에 선택할수 있는 모든 경우의 수를 확인 O(2^n)
  for i in range(1,len(require_key_list)+1):
    for j in combinations(require_key_list,i):
      union_require_key_list = set()
      sum_score = 0
      #경우의 수 들의 필요한 문자들을 합집합을 한 후 원소갯수 구해줌
      for require_key, score in j:
        union_require_key_list = union_require_key_list.union(require_key)
        sum_score += score
      #원소의 갯수가 n보다 작으면 이전 최댓값과 비교 후 더크면 대입
      if len(union_require_key_list) <= n:
        answer = max(answer,sum_score)
  return answer
  
print(solution(["ABcD", "bdbc", "a", "Line neWs"],7))