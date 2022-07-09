def solution(fuel, powers, distances):
    minimum = []
    for i in range(len(powers)):
        print(((2*distances[i])/powers[i])**0.5)
        minimum.append((2*distances[i]/powers[i])**0.5)
    minimum.sort(reverse=True)
    print(minimum[0])
    answer = 0
    return answer

# solution(8,[20, 30],[750, 675])
solution(19,[40, 30, 20, 10],[1000, 2000, 3000, 4000])