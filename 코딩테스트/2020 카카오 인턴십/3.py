# def check(buyDict:dict):
#     for i in buyDict.values():
#         if i == -1:
#             return False
#     return True 
    

# def solution(gems):
#     answer = []
#     minValue = int(1e9)
#     gemSet = set(gems)
#     buyDict = {gem: -1 for gem in gemSet}
    
#     for i in range(len(gems)):
#         buyDict[gems[i]] = i
#         if check(buyDict):
#             maxIndex = max(buyDict.values())
#             minIndex = min(buyDict.values())
#             if minValue > maxIndex - minIndex:
#                 minValue = maxIndex - minIndex
#                 answer = [minIndex+1, maxIndex+1]

#     return answer


from collections import defaultdict


def solution(gems):
    size = len(set(gems))
    n = len(gems)
    answer = [0, n-1]
    start = 0
    end = 0
    buyDict = defaultdict(int)
    buyDict[gems[0]] = 1
    
    while start < n and end < n:
        if len(buyDict) == size:
            if answer[1]-answer[0] > end - start:
                answer = [start, end]
            if buyDict[gems[start]] == 1:
                del buyDict[gems[start]]
            else:
                buyDict[gems[start]] -= 1
            start += 1
        else:
            end += 1
            if end >= n:
                break
            buyDict[gems[end]] += 1
    return [answer[0]+1, answer[1]+1]
            
            

# solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])