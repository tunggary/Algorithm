#이코테 349p
#아이디어: DFS를 이용한 완전 탐색, 전역 변수로 max min 구하기

n = int(input())
data = list(map(int, input().split()))
add,minus,mul,div = map(int, input().split())

max_value = -int(1e9)
min_value = int(1e9)

def dfs(count, value):
    global min_value, max_value, add, minus, mul, div
    if count == n:
        min_value = min(min_value, value)
        max_value = max(max_value, value)
    else:
        if add > 0:
            add -= 1
            dfs(count+1, value + data[count])
            add += 1
        if minus > 0:
            minus -= 1
            dfs(count+1, value - data[count])
            minus += 1
        if mul > 0:
            mul -= 1
            dfs(count+1, value * data[count])
            mul += 1
        if div > 0:
            div -= 1
            dfs(count+1, int(value / data[count]))
            div += 1
    
dfs(1,data[0])
print(max_value)
print(min_value)




