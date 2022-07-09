def solution(p):
    
    numDict = { i: 0 for i in range(len(p)) }
    i = 0
    
    for idx in range(len(p)):
        j = p.index(min(p[idx:]))
        if i != j:
            numDict[j] += 1
            numDict[i] += 1
            p[i], p[j] = p[j], p[i]
        i += 1
    
    return [i for i in numDict.values()]

