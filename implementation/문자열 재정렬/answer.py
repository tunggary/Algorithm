#이코테 332p
#아이디어: 아스키코드값으로 바꿔서 계산

 string = input()
 str_list = list(string)

 str_list.sort()

 result_num = 0
 result_string = ""

 for i in str_list:
   if i.isalpha():
     result_string += i
   else:
     result_num += int(i)

 print(result_string + str(result_num))
