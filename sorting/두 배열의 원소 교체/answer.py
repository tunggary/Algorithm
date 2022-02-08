#이코테 182p
#아이디어: 배열 B의 큰 값, A의 작은 값부터 두 원소를 비교하여 B의 값이 더 크면 교체

n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
  if(a[i]<b[i]):
    a[i],b[i] = b[i], a[i]
  else:
    break

print(sum(a))
