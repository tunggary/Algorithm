#이코테 377p
#아이디어: 탑다운 방식

n = int(input())
time = []
pay = []
dp = [-1]*(n+1)
max_value = 0

for _ in range(n):
    a, b = map(int, input().split())
    time.append(a)
    pay.append(b)
    
def next(day):
    if day >= n:
        return 0
    if dp[day] != -1:
        return dp[day]
    
    if day + time[day] <= n:
        dp[day] = max(next(day+1), pay[day]+next(day+time[day]))
    else:
        dp[day] = next(day+1)
    return dp[day]

next(0)
print(dp[0])