
def solution(survey, choices):
    answer = ''
    n = len(survey)
    result = {"A":0, "N":0, "C":0, "F":0, "M": 0, "J":0, "R":0, "T":0}
    for i in range(n):
        Non_agree = survey[i][0]
        Agree = survey[i][1]
        if choices[i] <= 3:
            result[Non_agree] += (4-choices[i])
        elif choices[i] >= 5:
            result[Agree] += (choices[i]-4)
            
    if result['R'] < result['T']:
        answer += 'T'
    else:
        answer += 'R'
    if result['C'] < result['F']:
        answer += 'F'
    else:
        answer += 'C'
    if result['J'] < result['M']:
        answer += 'M'
    else:
        answer += 'J'
    if result['A'] < result['N']:
        answer += 'N'
    else:
        answer += 'A'
    return answer