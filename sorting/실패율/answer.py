#이코테 361p
#아이디어: 각 스테이지에 도달한 유저 수 구하기

def solution(N, stages):
    total = len(stages)
    answer = []
    for i in range(1,N+1):
        if total == 0:
            answer.append((0.0, i))
            continue
        num = stages.count(i)
        answer.append((num/total, i))
        total -= num
    answer.sort(key=lambda x:(-x[0], x[1]))
    return [x[1] for x in answer]
