def checkVIP(price, period):
    if price >= 900000 and 24 <= period < 60:
        return True
    elif price >= 900000 and period >= 60:
        return True
    elif 600000 <= price < 900000 and period >= 60:
        return True
    return False

def solution(periods, payments, estimates):
    answer = [0,0]
    n = len(periods)
    for i in range(n):
        period = periods[i]
        totalPrice = sum(payments[i])
        n_peried = periods[i]+1
        n_totalPrice = totalPrice - payments[i][0] + estimates[i]
        vip = checkVIP( totalPrice, period,)
        n_vip = checkVIP(n_totalPrice, n_peried)
        if not vip and n_vip:
            answer[0] += 1
        elif vip and not n_vip:
            answer[1] += 1
        
    return answer

print(solution(
[24, 59, 59, 60], [[50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000], [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000], [350000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000], [50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000]], [350000, 50000, 40000, 50000]))