def solution(n, times):
    answer = 0
    dp = [int(1e9)]*(n+1)
    dp[1] = 0
    for i in range(2,n+1):
        if i % 2 == 0:
            for j in range(i//2,i-1):
                dp[i] = dp[j]+times[i-j]
    return answer