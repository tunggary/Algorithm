#유클리드 호제법을 이용한 최대공약수를 구하는 방법
#아이디어 : 두 수의 최대공약수를 구할 때 두 자연수 a,b에 대하여 (a>b) a를 b로 나눈 나머지를 r이라고 하자 이때 a와 b의 최대 공약수는 b와 r의 최대 공약수와 같다

def gcd(a,b):
  if a % b == 0:
    return b
  else:
    return gcd(b, a%b)

print(gcd(192,162))
  
