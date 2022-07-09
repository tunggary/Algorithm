from heapq import heappop, heappush


def solution(n, start, end, roads, traps):
    answer = 0
    graph_original = [[] for _ in range(n+1)]
    graph_reverse = [[] for _ in range(n+1)]
    for a,b,w in roads:
        graph_original[a].append((b,w))
        graph_reverse[b].append((a,w))
    
    reverse_check = [False]*(n+1)
    distance = [int(1e9)]*(n+1)
    distance[start] = 0
    q = []
    heappush(q,(0,start,True if start in traps else False))
    
    while q:
        dist, now, rev = heappop(q)
        if rev:
            for i in graph_reverse[now]:
                cost = dist + i[1]
                if distance[i[0]] > cost:
                    distance[i[0]] = cost
                    if i[0] in traps:
                        heappush(q, (cost, i[0], not reverse_check[i[0]]))
                        reverse_check[i[0]] = not reverse_check[i[0]]
                    else:
                        heappush(q, (cost, i[0], False))
        else:
            for i in graph_original[now]:
                cost = dist + i[1]
                if distance[i[0]] > cost:
                    distance[i[0]] = cost
                    if i[0] in traps:
                        heappush(q, (cost, i[0], not reverse_check[i[0]]))
                        reverse_check[i[0]] = not reverse_check[i[0]]
                    else:
                        heappush(q, (cost, i[0], False))
    print(distance)
    print(distance[end])

    return answer

# solution(3,1,3,[[1, 2, 2], [3, 2, 3]],[2])
solution(4,1,4,[[1, 2, 1], [3, 2, 1], [2, 4, 1]],[2, 3])