#이코테 377p
#아이디어: 퇴사일로부터 거꾸로 확인
n = int(input())
time = []
pay = []
dp = [-1]*(n+1)
max_value = 0

for _ in range(n):
    a, b = map(int, input().split())
    time.append(a)
    pay.append(b)
    
#i번째 날부터 얻을 수 있는 최대 수익
for i in range(n-1,-1,-1):
    next_day = time[i] + i
    
    if next_day <= n:
        dp[i] = max(pay[i]+dp[next_day], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value

print(max_value)
