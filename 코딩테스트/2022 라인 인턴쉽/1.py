from collections import defaultdict

def solution(logs:list[str]):
    info = set()
    info2 = defaultdict(int)
    people = set()
    
    for log in logs:
        name, quiz = log.split()
        info.add((quiz, name))
        people.add(name)
        
    for quiz, name in info:
        info2[quiz] += 1
    print(info2)
    answer = []
    for quiz, count in info2.items():
        if count >= len(people)/2:
            answer.append(quiz)
    return answer.sort()

solution(["morgan sort", "felix sort", "morgan sqrt", "morgan sqrt", "rohan reverse", "rohan reverse"])