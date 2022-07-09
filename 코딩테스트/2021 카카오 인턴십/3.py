# from collections import deque


# def solution(n, k, cmd):
#     answer = ['O' for i in range(n)]
#     excel = [i for i in range(n)]
#     current = k
#     delete = deque()
    
#     for each in cmd:
#         command = each.split()
#         if command[0] == 'U':
#             current -= int(command[1])
#         elif command[0] == 'D':
#             current += int(command[1])
#         elif command[0] == 'C':
#             exlen = len(excel)
#             delete.append(excel[current])
#             answer[excel[current]] = 'X'
#             del excel[current]
#             if current == exlen-1:
#                 current = exlen-2
#         else:
#             ele = delete.pop()
#             left = 0
#             right = len(excel)-1
#             while left <= right:
#                 mid = (left+right)//2
#                 if excel[mid] < ele:
#                     left = mid + 1
#                 else:
#                     right = mid - 1
#             excel = excel[:left] + [ele] + excel[left:]
#             if left <= current:
#                 current += 1
        
#     return ''.join(answer)


def solution(n, k, cmd):
    answer = ['O' for _ in range(n)]
    linked_list = {i:[i-1, i+1] for i in range(n)}
    delete_stack = []
    current = k
    for each in cmd:
        command = each.split()
        if command[0] == 'U':
            for _ in range(int(command[1])):
                current = linked_list[current][0]
        elif command[0] == 'D':
            for _ in range(int(command[1])):
                current = linked_list[current][1]
        elif command[0] == 'C':
            prev,next = linked_list[current]
            answer[current] = 'X'
            delete_stack.append((prev,next,current))
            if next == n:
                current = linked_list[current][0]
            else:
                current = linked_list[current][1]
            
            if prev == -1:
                linked_list[next][0] = prev
            elif next == n:
                linked_list[prev][1] = next
            else:
                linked_list[next][0] = prev
                linked_list[prev][1] = next
        else:
            prev,next,position = delete_stack.pop()
            answer[position] = 'O'
            if prev == -1:
                linked_list[next][0] = position
            elif next == n:
                linked_list[prev][1] = position
            else:
                linked_list[next][0] = position
                linked_list[prev][1] = position
                
    return ''.join(answer)

print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))