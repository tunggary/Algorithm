def getDist(nx,ny,x,y):
    return abs(nx-x)+abs(ny-y)

def getHorDist(ny,y):
    return abs(ny-y)

def solution(line):
    answer = []
    keyPos = {"1": (0,0),"2": (0,1),"3": (0,2),"4": (0,3),"5": (0,4),"6": (0,5),"7": (0,6),"8": (0,7),"9": (0,8),"0": (0,9),"Q": (1,0),"W": (1,1),"E": (1,2),"R": (1,3),"T": (1,4),"Y": (1,5),"U": (1,6),"I": (1,7),"O": (1,8),"P": (1,9)}
    commands = list(line)
    lx, ly = 1, 0
    rx, ry = 1, 9
    
    for input in commands:
        nx, ny = keyPos[input]
        leftDist = getDist(nx,ny,lx,ly)
        rightDist = getDist(nx,ny,rx,ry)
        if leftDist == rightDist:
            leftHorDist = getHorDist(ny,ly)
            rightHorDist = getHorDist(ny,ry)
            if leftHorDist == rightHorDist:
                if ny > 4:
                    answer.append(1)
                    rx, ry = nx, ny
                else:
                    answer.append(0)
                    lx, ly = nx, ny
            elif leftHorDist > rightHorDist:
                answer.append(1)
                rx, ry = nx, ny
            else:
                answer.append(0)
                lx, ly = nx, ny
        elif leftDist > rightDist:
            answer.append(1)
            rx, ry = nx, ny
        else:
            answer.append(0)
            lx, ly = nx, ny
    return answer

print(solution("Q4OYPI"))
    