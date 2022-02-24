#이코테 370p
#아이디어: 
#1. 문자열의 길이별로 검색을 해야함 
#2. ?를 a~z사이에 모든 값을 올 수 있음을 이용하여 이진 탐색을 실행 
#3. ?가 접두사에 오는 경우 뒤집어서 이진탐색을 실행

from bisect import bisect_left, bisect_right

def count_by_range(array, min_value, max_value):
    l_index = bisect_left(array, min_value)
    r_index = bisect_right(array, max_value)
    return r_index - l_index
    
def solution(words, queries):
    array = [[] for i in range(10001)]
    r_array = [[] for i in range(10001)]
    n = len(words)
    answer = []
    for word in words:
        array[len(word)].append(word)
        r_array[len(word)].append(word[::-1])
        
    for i in range(1,10001):
        array[i].sort()
        r_array[i].sort()

    for query in queries:
        if query[0] != '?':
            count = count_by_range(array[len(query)], query.replace('?','a'), query.replace('?','z'))
        else:
            count = count_by_range(r_array[len(query)], query[::-1].replace('?','a'), query[::-1].replace('?','z'))
        answer.append(count)
    return answer
