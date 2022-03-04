#이코테 483p
#아이디어: prefix sum(접두사 합)을 이용하여 문제를 O(n+m)의 시간 복잡도안에 해결할 수 있다.

n, data = 5, [10,20,30,40,50]

sum_value = 0
prefix_sum = [0]

for i in data:
    sum_value += i
    prefix_sum.append(sum_value)
    
left, right = 3, 4
print(prefix_sum[right] - prefix_sum[left-1])