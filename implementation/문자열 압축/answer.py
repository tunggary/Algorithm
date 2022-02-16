#이코테 323p
#아이디어: 모든 압축할 수 있는 경우(1 ~ len(str)//2)에 대해서 압축을 하여 최소값 구함

def solution(s):
    answer = len(s)
    
    for step in range(1, len(s)//2 + 1):
        compressed = ""
        count = 1
        prev = s[0:step]
        
        for j in range(step, len(s), step):
            now = s[j:j+step]
            if prev == now:
                count += 1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                count = 1
                prev = now
        compressed += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compressed))

    return answer
