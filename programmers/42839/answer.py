from itertools import permutations

def is_prime(x):
  if x <= 1:
    return False
  for i in range(2,int(x**0.5)+1):
    if x % i == 0:
      return False
  return True

# def solution(numbers):
#   answer = set()
#   numberList = list(numbers)
#   for n in range(1,len(numbers)+1):
#     for i in permutations(numberList, n):
#       number = int(''.join(i))
#       if is_prime(number):
#         answer.add(number)
  # return len(answer)

primeSet = set()


def isPrime(number):
    if number in (0, 1):
        return False
    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def makeCombinations(str1, str2):
    if str1 != "":
        if isPrime(int(str1)):
            primeSet.add(int(str1))

    for i in range(len(str2)):
        print(str1 + str2[i])
        makeCombinations(str1 + str2[i], str2[:i] + str2[i + 1:])


def solution(numbers):
    makeCombinations("", numbers)

    answer = len(primeSet)

    return answer

solution("1234")
