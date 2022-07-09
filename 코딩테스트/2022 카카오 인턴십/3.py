def solution(alp, cop, problems:list[list]):
    answer = 0
    max_alp_req = 0
    max_cop_req = 0
    for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
        max_alp_req = max(alp_req, max_alp_req)
        max_cop_req = max(cop_req, max_cop_req)
        
        
    return answer