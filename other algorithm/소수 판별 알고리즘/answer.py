#이코테 468p
#아이디어: 약수는 가운데 약수(제곱급)을 기준으로 대칭이므로 소수 판별 또한 제곱근 까지만 확인하여 시간복잡도를 줄인다.

def is_prime_number(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True
