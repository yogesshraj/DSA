# print(True, end= " "); print(False)
# print(f"Yogi {1}")

# print('I am', 35,'years old', sep = '')

# x,y,z = 1,2,3
# x = y = z = 'orange'
# z= ""
# print(x,y, z)


# x = 1
# def func(x):
#     for i in range(10):
#         x += 1
#         print(x)
#     # global x
#     print(x)
# func(x)

# print(x)

# print(2e2)
# print(5+2j)

# print(int("4"))

# b = '''yogi is
# greates 
# of 
# all time '''

# for i in b: 
#     print(i)

# print(len(b))

# z = 'Hello World'
# print(z[-5:])

# print(z.replace('Hello', "goodbye"))


# g = 3

# print(f'yogi is {g:.1f}')

# c= 'Hello\nworld\nwog'
# print(c)
# print(c.replace('\n', '\r\r'))

# h = "Hello\r\rWorld"
# print(h)

# a = '\n'
# print(3*a,"weg")

# we= 'Hello\nWorld'
# print(we, "\133")

# print("YoGi".casefold())

# print(we .center(20,"a"))

# print ('banana'.find('super', 1, 5))

# print("banana".rjust(20, "@"))
# print("bananna","ho")

# op = 'Yogi is greatest of all time'
# trans = str.maketrans("ogi","esa")
# print(op.translate(trans))
# print("banana  ".strip("ba"))

# print(op.partition('all'))

# print('banana an'.rfind('an'))

# print("you are an idiot an apple".rpartition('an'))

# print('a,b,c,d'.rsplit(',', 2))

# print(6%2)

# # n = int(input())

# # if(str(n).isdecimal()):
# #     for i in range(n):
# #         print(i**2)

# print('banana'.count("an"))


# print(1 < 5 < 10)

# x = [1, 2, 3]
# y = [1, 2, 3]
# z = list(x)
# z.append("4")
# print(id(x), id(y), id(z))
# print(x, z)

# a = [1,2,3]
# b = [1,2,3]
# c = a
# print(a is not b)
# print(a == b )
# print(a is b)
# print(a is c)

# print(3 not in a)


# lo = "hello"
# print( 'heo' in lo)

# print(3**2+(5-(2*8)))

# print(list((1,2,3)))

# print("geello"[2:3])

# wow = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'fruit']
# wow[1:4] = ["pumking", 'seekds']
# print(wow)

# del wow
# # print(wow)

# wows = [1,2,3]
# wows = []
# print(wows)
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# print([i for i in fruits if 'a' in i])

# thislist = ['Yo','don', 'of', 'SalesCaptain']
# thislist.sort(key=len and str.upper)
# print(thislist)

# po = [1,2,3,4]
# ci = po[:2]
# ci = []
# for i in range(2):
#     ci.append(po[i])
# print(ci)
# print(0 == True)

# dr = {1,2,3}
# # print(dr[1])

# kol = {
#     "a": 1,
#     "b": 2,
#     "c": 3
# }
# kol.get("d", 3)
# print(kol)
# # for i in kol.keys():
# #     print(i)

# # for i in kol.items():
# #     print(i)
# # print(kol.items())

# c = kol.pop("a")
# print(c)

# pii= ''
# # pii+= 1
# print(pii)

# N = input()

# if N.isalpha():
#     ""
# elif N.find('.') == -1 or N.find('+') != -1 and N.find("-") != -1:
#     print (False)
# else:
#     final = False
#     for i in N:
#         if i.isalpha():
#             print (False)
#             final = False
#             break
#         else:
#             final = True

#     if final:
#         print(final)

# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())

# a = []
# b = []
# for i in range(0,x+1):
#     for j in range(0, y+1):
#         for k in range(0, z +1):
#             b.append([i,j,k])
#             if i+j+k != n:
#                 a.append([i,j,k])

# print([[i,j,k] for i in range(0, x+1) for j in range(0, y+1) for k in range(0, z +1) if i+j+k != n ])
# print(b)


# print('1anana'.index("n",3))
# print('1anana'.rindex("n",3))
# print('1anana'.count("wow",3))
# print('1anana'.find("wow",3))
# print('1anana'.rfind("wow",3))

# print('1anana'.center(8,"*"))
# print('1anana'.ljust(8,"*"))
# print('1anana'.rjust(8,"*"))

# print("banana".isupper())
# print("Banana".upper())
# print("banana".islower())
# print("Banana".lower())
# print("Banana".istitle())
# print("banana".capitalize())

# print('banana'.strip("an"))
# print('banana'.lstrip("an"))
# print('banana'.rstrip("an"))

# print('one love one shit'.replace("one","two"))

# print('one love one shit'.split(" ",2))
# print('one love one shit'.rsplit(" ",2))

# a = 343.53234523
# b= 343.53234523
# c = a

# print(a == b)
# print(a is b)

# print([1,2,3])
# print(list((1,2,3)))

# ipo = list((1,2,3))
# ipo.append("wo")
# print(ipo)
# ipo.insert(1,"wow")
# print(ipo)

# ipo.extend([4,5,6])
# print(ipo)

# ipo.pop()
# print(ipo)
# ipo.pop(0)
# print(ipo)

# del ipo[2]
# print(ipo)

# # ipo.clear()
# # print(ipo)

# for i in ipo:
#     print(type(i))

# for i in range(len(ipo)):
#     print(i)

# print([i for i in ipo if isinstance(i, int)])
# print([ipo[i] for i in range(len(ipo)) if i > 2])

# a = [1,2,3]
# b = a.copy()
# c = a[:]
# d = list(a)
# print(a.count(2))

# lk = [4,7,2,7,1,6]
# # lk.sort(reverse=True, key=len)
# print(lk)
# a,b,*c = lk
# print(a,b,c)
# # tuple is something where duplicates can exist, ordered, but the values can't be add or updated.
# wh = (1,2,3,4)
# # del wh[0]
# print(wh)

# #set is something where it is unordered. you can add/update delete index but duplicate can't exist.

# wow_set = {"ab","ew","wr"}

# wow_set.add("yo")
# wow_set.discard("ew")
# # wow_set.remove("wrr") it will throw error if the deleting entity is not present.

# print(wow_set)


# superman = {
#     "a" : "batman",
#     "b" : "spiderman",
#     "c" : "ironman",
#     "d" : "antman",
# }

# superman["d"] = 'he-man'
# superman.update({"a": "wonderwomen", "e": "aquaman"})
# print(superman)
# del superman["a"]
# # superman.pop("a")
# print(superman.keys(), superman.values(), superman.items())
# print(superman["b"], superman.get("b"))

# a = 330
# b = 330
# print(a if a > b else b if b > a else a,b )


# zep = 30
# day = 1
# match zep:
#     case 10:
#         print("wow")
#     case 20 | 30 if day == 2:
#         print("zooper")
#     case 30 if day == 3:
#         print("nothing")
#     case _:
#         print("shit")


# stud_details = []
# top_score = []
# second_score_studs =[]
# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     stud_details.append([name, score])
#     if score not in top_score:
#         top_score.append(score)

# print(stud_details.sort())
# final_top_score = top_score.sort()
# print(stud_details, final_top_score)
# for i in stud_details:
#     if i[1] == final_top_score[1]:
#         second_score_studs.append(i[0])
# second_score_studs.sort()
# for i in second_score_studs:
#     print(i)

# stud_details = []
# least_score = 0
# second_least_score = 0
# final_arr = []
# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     stud_details.append([name, score])
#     if least_score == 0 and second_least_score == 0:
#         least_score = score
#         second_least_score = score
#     elif score < least_score:
#         second_least_score = least_score
#         least_score = score
#     elif least_score < score < second_least_score:
#         second_least_score = score

# if 2<= len(stud_details) <=5:
#     for i in stud_details:
#         if i[1] == second_least_score:
#             final_arr.append(i[0])
#     final_arr.sort()
#     for i in final_arr:
#             print(i)
    

    # 5 Prashant 52.22 Kush 52.223 Kant 52.222 Kanti 52.2222 Harshit 52.22222


# n = int(input())
# arr = map(int, input().split())

# converted = list(arr)
# flag = False
# if 2 <= n <= 10:
#     for i in converted:
#         # print (i)
#         if -100 <= i <= 100:
#             if n == len(converted):
#                 flag = True
# if(flag):
#     b = set(converted)
#     c = list(b)
#     c.sort()
#     print(c[len(c)-2])


# n = int(input())
# student_marks = {}
# for _ in range(n):
#     name, *line = input().split()
#     scores = list(map(float, line))
#     student_marks[name] = scores
    
# query_name = input()
# marks = student_marks.get(query_name)
# if(marks is not None):
#     print_value = sum(marks)/len(marks) 
#     print(f"{print_value:.2f}")

    
# records = []
# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     records.append([name, score])

# least_score = None
# second_least_score = None
# for i in records:
#     if least_score is None:
#         least_score = i[1] 
#     elif least_score > i[1]:
#         least_score = i[1]

# for i in records:
#     if second_least_score is None and i[1] != least_score:
#         second_least_score = i[1]
#     elif i[1] != least_score and i[1] > least_score and second_least_score > i[1]:
#         second_least_score = i[1]

# second_least_score_arr = []
# for i in records:
#     if i[1] == second_least_score:
#         second_least_score_arr.append(i[0])

# second_least_score_arr.sort()
# for i in second_least_score_arr:
#     print(i)



# arr = []
# N = int(input())
# for i in range(N):
#     get_input = str(input())
#     if get_input.find('insert') != -1:
#         arr.insert(int(get_input.split(' ')[1]),int(get_input.split(' ')[2]))
#     elif get_input.find('print') != -1:
#         print (arr)
#     elif get_input.find('remove') != -1:
#         for i in range(len(arr)):
#             if arr[i] == int(get_input.split(' ')[1]):
#                 arr.pop(i)
#                 break
#     elif get_input.find('append') != -1:
#         arr.append(int(get_input.split(' ')[1]))
#     elif get_input.find('sort') != -1:
#         arr.sort()
#     elif get_input.find('pop') != -1:
#         arr.pop()
#     elif get_input.find('reverse') != -1:
#         arr.reverse()

# n = int(input())
# second_inmput = str(input())
# second_inmput = second_inmput.split(' ')
# for i in range(len(second_inmput)):
#     second_inmput.insert(i, int(second_inmput[i]))
#     second_inmput.pop(i+1)

# # print(second_inmput)
# if len(second_inmput) == n:
#     this_tuple = tuple(second_inmput)
#     print(this_tuple)
#     print(hash(this_tuple))
#     print(hash(("1","2")))


# n = int(input())
# # Reads the line "1 2", splits it to ['1', '2'], and map(int, ...) 
# # converts it to a sequence of integers, which is then cast to the tuple (1, 2)
# integer_tuple = tuple(map(int, input().split()))

# # Calculates and prints the hash of the tuple (1, 2)
# print(hash(integer_tuple))


# def swap_case(s):
#     s.swapcase()
#     return s.swapcase()

# if __name__ == '__main__':
#     n = str(input())
#     print(swap_case(n))

# def split_and_join(line):
#     line_arr = line.split(' ')
#     line_join = "-".join(line_arr)
#     return line_join

# if __name__ == '__main__':
#     line = input()
#     result = split_and_join(line)
#     print(result)

# def print_full_name(first, last):
#     print( f'Hello {first} {last}! You just delved into python.')

# if __name__ == '__main__':
#     first_name = input()
#     last_name = input()
#     print_full_name(first_name, last_name)


# def mutate_string(string, position, character):
#     return string[:position] + character + string[(position+1):]

# if __name__ == '__main__':
#     s = input()
#     i, c = input().split()
#     s_new = mutate_string(s, int(i), c)
#     print(s_new)

# a =[2,1]
# print(a[1:4])
# def count_substring(string, sub_string):
#     total_count = 0
#     for i in range(len(string)):
#         if sub_string == string[i:(i+len(sub_string))]:
#             total_count += 1
#     return total_count

# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
    
#     count = count_substring(string, sub_string)
#     print(count)


# if __name__ == '__main__':
    # s = input()
    # is_alnum= False
    # is_alpha= False
    # is_digit= False
    # is_lower= False
    # is_upper= False
    # for i in s:
    #     if i.isalnum() and is_alnum != True:
    #         is_alnum = True
    #     if i.isalpha() and is_alpha != True:
    #         is_alpha = True
    #     if i.isdigit() and is_digit != True:
    #         is_digit = True
    #     if i.islower() and is_lower != True:
    #         is_lower = True
    #     if i.isupper() and is_upper != True:
    #         is_upper = True
    # print(is_alnum, is_alpha, is_digit, is_lower, is_upper, sep='\n')

#Replace all ______ with rjust, ljust or center. 

# thickness = int(input()) #This must be an odd number
# c = 'H'

# #Top Cone
# for i in range(thickness):
#     print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

# #Top Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

# # #Middle Belt
# for i in range((thickness+1)//2):
#     print((c*thickness*5).center(thickness*6))    

# # #Bottom Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

# # #Bottom Cone
# for i in range(thickness):
#     print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

# import textwrap

# def wrap(string, max_width):
#     totals_str = ''
#     for i in range(0, len(string), max_width):
#         printable_str = ''
#         for j in range(max_width):
#             if i < len(string):
#                 printable_str+= string[i]
#                 i+=1
#         totals_str += (f"{printable_str}\n" if i < len(string) else printable_str)

#     return totals_str

# if __name__ == '__main__':
#     string, max_width = input(), int(input())
#     result = wrap(string, max_width)
#     print(result)


# import math
# h, w = input().split()
# height= int(h)
# width = int(w)
# center_line_count = math.ceil(height / 2)
# multiplier = 1
# for i in range(1, height+1):
#     if center_line_count != i:
#         style_chract = ".|."
        
#         print((style_chract*multiplier).center(width,"-"))
#         if i < center_line_count:
#             multiplier += 2
#         else:
#             multiplier -= 2
#     else:
#         print('WELCOME'.center(width,"-"))
#         multiplier -= 2

# multiplier = 1
# for i in range(1,50):
#     print(multiplier)
#     multiplier += 2 

# def print_formatted(number):
#     bin_length = len(bin(number).lstrip("0b"))
#     for i in range(1,number+1):
#         print(f"{i}".rjust(bin_length," " ), f"{oct(i).lstrip("0o")}".rjust(bin_length," " ), f"{hex(i).lstrip("0x").capitalize()}".rjust(bin_length," " ), f"{bin(i).lstrip("0b")}".rjust(bin_length," " ))

# if __name__ == '__main__':
#     n = int(input())
#     print_formatted(n)


# import string
# def print_rangoli(size):
#     total_string = []
#     for i in string.ascii_lowercase[:size]:
#         total_string.insert(0,i)
        
#     cloned_total_string = list(total_string)
#     cloned_total_string.reverse()


#     if cloned_total_string[0] == total_string[len(total_string)-1] :
#         cloned_total_string.pop(0)
#     base="-".join(total_string+cloned_total_string)

#     multiplier = 1
#     for i in range(1,size+1):
#         sum_machine = ("-".join(total_string[:i] + cloned_total_string[(size-i):])).center(len(base),"-")
#         if (i == size):
#             for j in range(size,0,-1):
#                 neg_sum_machine = ("-".join(total_string[:j] + cloned_total_string[(size-j):])).center(len(base),"-")
#                 print(neg_sum_machine)
#         else:
#             print(sum_machine)
#         multiplier += 2


# if __name__ == '__main__':
#     n = int(input())
#     print_rangoli(n)


# from datetime import datetime, timezone

# a = datetime.now()
# print(a.year,a.day, a.month)

# print(timezone.dst())

# import math
# print(math.sqrt(25))
# print(min([5,7,8,4]))
# print(max([5,7,8,4]))

# print(pow(4,2))

# print(math.ceil(4.9))
# print(math.floor(4.9))

# print(math.ceil(4.2))
# print(math.floor(4.2))

# import math
# import os
# import random
# import re
# import sys

# def solve(s):
#     return s
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     s = input()

#     result = solve(s)

#     fptr.write(result + '\n')

#     fptr.close()


def minion_game(string):
    vowels = ["A", "E", "I", "O", "U"]
    # vowel_user_calc:
    vowel_check = check_vowels(string, vowels)
    total_vowel_words = []
    for j in vowel_check:
        remaining_str = list(string[j:])
        for i in range(len(remaining_str)):
            total_vowel_words.append("".join(remaining_str))
            remaining_str.pop()
    
    total_vowel_words_2 = list(set(total_vowel_words))
    score = 0
    for i in total_vowel_words_2:
        for j in range(len(s)):
            if s.startswith(i,j):
                score+=1
    print(score)

    # non_vowel_user_calc:
    non_vowel_check = check_non_vowels(string, vowels)
    total_non_vowel_words = []
    for j in non_vowel_check:
        remaining_str = list(string[j:])
        for i in range(len(remaining_str)):
            total_non_vowel_words.append("".join(remaining_str))
            remaining_str.pop()
    
    total_non_vowel_words_2 = list(set(total_non_vowel_words))
    non_vowel_score = 0
    for i in total_non_vowel_words_2:
        for j in range(len(s)):
            if s.startswith(i,j):
                non_vowel_score+=1
    print(non_vowel_score)
    if(score > non_vowel_score):
        print(f"Kevin {score}")
    else:
        print(f"Stuart {non_vowel_score}")

def check_vowels(string, vowels):
    return_arr = []
    for i in range(len(string)):
        for j in vowels:
            if string[i] == j:
                return_arr.append(i)
    return list(set(return_arr))  

def check_non_vowels(string, vowels):
    return_arr = []
    for i in range(len(string)):
        for j in vowels:
            if string[i] != j:
                return_arr.append(i)
            else:
                break
    return list(set(return_arr))  
    
if __name__ == '__main__':
    s = input()
    minion_game(s)