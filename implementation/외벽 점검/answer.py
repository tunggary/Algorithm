#이코테 335p
#아이디어: 친구들을 뽑은 후 순서도 중요함으로 순열을 사용

from itertools import permutations
def solution(n, weak, dist):
    weakSize = len(weak)
    weak = weak + [w+n for w in weak]
    answer = int(1e9)
    
    for start in range(weakSize):
        for d in permutations(dist, len(dist)):
            prevPos = start
            count = 1
            for i in range(1,weakSize):
                pos = start + i
                distance = weak[pos] - weak[prevPos]
                if distance > d[count-1]:
                    count += 1
                    prevPos = pos
                if count > len(dist):
                    break
            if count <= len(dist):
                answer = min(answer, count)
    if answer == int(1e9):
        return -1
    return answer
