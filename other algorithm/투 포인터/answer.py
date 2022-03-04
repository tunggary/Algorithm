#이코테 476p
#아이디어: 특정한 합을 가지는 부분 연속 수열 찾기 문제에서 투 포인터 알고리즘을 이용하여 해결한다.

n,m,data = 5, 5, [1,2,3,2,5]
count, interval_sum, end = 0, 0, 0

for start in range(n):
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]
    
print(count)