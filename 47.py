fish_num = [[0]*4 for _ in range(4)]
fish_dir = [[0]*4 for _ in range(4)]

for i in range(4):
    data = list(map(int, input().split()))
    for j in range(8):
        if j % 2 == 0:
            fish_num[i][j//2] = data[j]
        else:
            fish_dir[i][j//2] = data[j]
            
print(fish_num)
print(fish_dir)