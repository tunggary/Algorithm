#이코테 99p
#정당성 : 입력 조건에서 K는 2보다 큼으로 나누는 것이 항상 1을 빼는것 보다 더 작아진다.

# n,k = map(int, input().split())
# count = 0

 while n != 1:
   if n % k == 0:
     n //= k
   else:
     n -= 1
   count += 1

 print(count)
