#백준 11723번
import sys
n = int(sys.stdin.readline())
s = set()

for _ in range(n):
    input_data = sys.stdin.readline().strip().split()
    if len(input_data) == 1:
        if input_data[0] == 'all':
            s = set([i for i in range(1,21)])
        else:
            s = set()
        continue

    command, num = input_data[0], int(input_data[1])
    if command == 'add':
        s.add(num)
    elif command == 'remove':
        s.discard(num)
    elif command == 'check':
        print(1) if num in s else print(0)
    elif command == 'toggle': 
        if num in s:
            s.discard(num)
        else:
            s.add(num)
        