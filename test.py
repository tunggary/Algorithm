keyboard = [["가","호","저","론","남","드","부","이","프","설"],
            ["알","크","청","울","키","초","트","을","배","주"],
            ["개","캠","산","대","단","지","역","구","너","양"],
            ["라","로","권","교","마","쿼","파","송","차","타"],
            ["코","불","레","뉴"," ","서","한","산","리","개"],
            ["터","강","봄","토","캠","상","호","론","운","삼"],
            ["보","람","이","경","아","두","프","바","트","정"],
            ["스","웨","어","쿼","일","소","라","가","나","도"],
            ["판","자","비","우","사","거","왕","태","요","품"],
            ["안","배","차","캐","민","광","재","봇","북","하"]]

def findPos(word, first=False):
    ret = []
    for row in range(10):
        for col in range(10):
            if keyboard[row][col] == word:
                ret.append((col, row))
                if first:
                    return ret
    if len(ret) == 0:
        return -1
    else:
        return ret

def solution(word):
    answer = [0,0]
    prev = findPos(word[0], True)
    for i in range(1, len(word)):
        next = findPos(word[i])
        if prev == -1:
            answer[0] += 20
            answer[1] += 1
            prev =  -1 if next == -1 else [(next[0][0], next[0][1])] 
        
            continue
        elif next == -1:
            prev = next
            continue
        MIN = int(1e9)
        MIN_pos = [0,0]
        for p_row, p_col in prev:
            for n_row, n_col in next:
                dist = abs(p_row - n_row) + abs(p_col - n_col) 
                if MIN > dist:
                    MIN = dist
                    MIN_pos[0] = n_col
                    MIN_pos[1] = n_row
        answer[0] += MIN
        answer[1] += 1
        prev = [(MIN_pos[1],MIN_pos[0])]
        
    return answer
        
            

print(solution("가산"))