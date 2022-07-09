from itertools import permutations

def check(user_id:str, banned_id:str):
    n = len(user_id)
    m = len(banned_id)
    if n != m:
        return False
    for i in range(n):
        if banned_id[i] == '*':
            continue
        if banned_id[i] != user_id[i]:
            return False
    return True
            
def solution(user_id:list[str], banned_id:list[str]):
    answer = []
    user_permutations = permutations(user_id, len(banned_id))
    for user_list in user_permutations:
        count = 0
        for user,banned in zip(user_list,banned_id):
            if check(user,banned):
                count += 1
        if count == len(banned_id):
            if set(user_list) not in answer:
                answer.append(set(user_list)) 
    return len(answer)   

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "*rodo", "******", "******"]))