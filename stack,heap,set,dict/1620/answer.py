#백준 1620번

n,m = map(int, input().split())
data1 = dict()
data2 = dict()
for i in range(1, n+1):
    string = input()
    data1[string] = i
    data2[str(i)] = string
for _ in range(m):
    input_data = input()
    if input_data.isalpha():
        print(data1[input_data])
    else:
        print(data2[input_data])
