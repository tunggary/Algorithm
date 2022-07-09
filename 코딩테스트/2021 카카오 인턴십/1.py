def solution(s:str):
    answer = ""
    current = ""
    transform = {
	    "zero":"0",
	    "one":"1",
	    "two":"2",
	    "three":"3",
	    "four":"4",
	    "five":"5",
	    "six":"6",
	    "seven":"7",
	    "eight":"8",
	    "nine":"9"
    }
    for char in s:        
        if char.isdigit():
            answer += char
        else:
            current += char
            
        if transform.get(current):
           answer += transform[current]
           current = ""
    return int(answer)

print(solution("one4seveneight"))