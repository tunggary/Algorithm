

def ShiftRow(rc):
    rc.insert(0, rc[-1])
    return rc[:-1]
    

def Rotate(rc):
    backup = 0
    colLen = len(rc[0])
    rowLen = len(rc)
    for col in range(colLen-1,0,-1):
        if col == colLen - 1:
            backup = rc[0][col]
            rc[0][col] = rc[0][col-1]
        else:
            rc[0][col] = rc[0][col-1]
            
    for row in range(rowLen-1,0,-1):
        if row == 1:
            rc[row][colLen-1] = backup
        elif row == rowLen-1:
            backup2 = rc[row][colLen-1]
            rc[row][colLen-1] = rc[row-1][colLen-1]
        else:
            rc[row][colLen-1] = rc[row-1][colLen-1]
    
    for col in range(colLen-1):
        if col == 0:
            backup3 = rc[rowLen-1][col]
            rc[rowLen-1][col] = rc[rowLen-1][col+1]
        elif col == colLen - 2:
            rc[rowLen-1][col] = backup2
        else:
            rc[rowLen-1][col] = rc[rowLen-1][col+1]
    
    for row in range(rowLen-1):
        if row == rowLen-2:
            rc[row][0] = backup3
        else:
            rc[row][0] = rc[row+1][0]

def solution(rc, operations):    
    for operation in operations:
        if operation == 'ShiftRow':
            rc = ShiftRow(rc)
        else:
            Rotate(rc)
    return rc

solution([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],["rotate"])
