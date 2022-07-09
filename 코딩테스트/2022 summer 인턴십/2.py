from collections import defaultdict

def solution(rooms, target):
    seatInfo = defaultdict(set)
    for room in rooms:
        splitData = room.split(',')
        if splitData[0][4] == ']':
            roomNum = splitData[0][1:4]
            splitData[0] = splitData[0][5:]
        else:
            roomNum = splitData[0][1:5]
            splitData[0] = splitData[0][6:]
            
        for name in splitData:
            seatInfo[name].add(int(roomNum))
            
    sortData = []    
    for name, rooms in seatInfo.items():
        if target in rooms:
            continue
        nearestValue = int(1e9)
        for room in rooms:
            if abs(room - target) < nearestValue:
                nearestValue = abs(room - target)
        sortData.append((len(rooms), nearestValue, name))
    sortData.sort()
    return [name for _,_,name in sortData]

print(solution(["[403]James", "[404]Azad,Louis,Andy", "[101]Azad,Guard"],403))

