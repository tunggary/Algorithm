def solution(atmos):
    answer = 0
    recycle = 0
    mask = False
    for a, b in atmos:
        if a >= 81 or b >= 36:
            if mask:
                recycle += 1
                if (a >= 151 and b >= 76) or recycle >= 3:
                    recycle = 0
                    mask = False
            else:
                answer += 1
                mask = True
                recycle += 1
                if (a >= 151 and b >= 76) or recycle >= 3:
                    recycle = 0
                    mask = False
        else:
            if mask:
                recycle += 1
                if recycle >= 3:
                    recycle = 0
                    mask = False

    return answer

print(solution([[80, 35], [70, 38], [100, 41], [75,30], [160,80], [77, 29], [181, 68], [151, 76]]))