#answer1.py에 정답은 시간 복잡도가 O(N) 이다.
#answer2.py에 정답은 시간 복잡도가 O(logN)이다. 즉 N이 기하급수적으로 커졌을 때 사용할 수 있다.

 n,k = map(int, input().split())
 count = 0

 while True:
   #target : n과 가장 가까운 k로 나누어 떨어질 수 있는 수
   target = (n//k)*k
   count += (n - target) #n이 target이 될때까지 1을 뺀다고 생각
   n = target

   #n(위에서 target)이 k보다 작으면 break
   if n < k:
     break;
  
   #n이 k로 나누어질수 있음으로 k로 나누고 count를 증가
   count += 1
   n //= k

 #n이 k보다 작아서 빠져나온 경우, 나머지 수를 1이 될때까지 1씩 뺌
 count += (n-1)
 print(count)
