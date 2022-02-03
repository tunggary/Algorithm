#answer1.py의 방식은 시간 복잡도가 O(M)이므로 M의 크기가 기하급수적으로 커질때 시간초과가 될 것이다.
#answer2.py의 방식은 시간 복잡도가 O(1)이므로 M의 크기가 기하급수적으로 커질때 효과적이다.
#정당성 : first + first + ... + first + second 즉, 이처럼 K개의 first와 한개의 second의 패턴이 반복되는 방식이므로 이를 한번에 구해 더할 수 있다.

n, m, k = map(int, input().split())
data = list(map(int, input().split()))
result = 0

data.sort(reverse = True)
first = data[0]
second = data[1]

#패턴 하나의 길이가 k+1이므로, m을 k+1로 나눈 몫을 패턴 하나의 값을 곱한다.
result += (m//(k+1))*(first*k + second])
#m이 k+1로 나누어 떨어지지 않았을 때, 남은 수는 전부 first이므로 나머지 곱하기 first를 해준다. 
result += (m%(k+1))*first

print(result)
