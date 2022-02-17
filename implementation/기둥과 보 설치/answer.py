#이코테 329p
#아이디어: 설치, 삭제 할 때마다 가능한지 체크

def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0:
            if y == 0 or [x-1,y,1] in answer or [x,y,1] in answer or [x, y-1, 0] in answer:
                continue
            else:
                return False
        if stuff == 1:
            if ([x-1,y,1] in answer and [x+1,y,1] in answer) or [x,y-1,0] in answer or [x+1,y-1,0] in answer:
                continue
            else:
                return False
    return True

def solution(n, build_frame):
    answer = []
    for x,y,stuff,operate in build_frame:
        if operate == 1:
            answer.append([x,y,stuff])
            if not possible(answer):
                answer.remove([x,y,stuff])
        if operate == 0:
            answer.remove([x,y,stuff])
            if not possible(answer):
                answer.append([x,y,stuff])
        
    return sorted(answer)
