# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, 
# если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. 
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, 
# если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  

#Вариант 1

def pooh(string):
    n = 0
    for i in string:
       if i == "а" or i == "у" or i == "е" or i == "ы" or i == "о" or i == "э" or i == "я" or i == "и" or i == "ю":
          n+=1
       else:
           n+=0
    return n
      
    
string_1 = "ПАра-ра-рам"
string_2 = "рам-пам-папам" 
string_3 = "па-ра-па-да"

string_11 = string_1.lower()
string_22 = string_2.lower()
string_33 = string_3.lower()

if pooh(string_11) == pooh (string_22) == pooh (string_33):
    print ("Парам пам-пам")
else:
    print ("Пам парам")

#Вариант 2

string_1 = str(input())
string_2 = str(input()) 
string_3 = str(input())

string_11 = string_1.lower()
string_22 = string_2.lower()
string_33 = string_3.lower()

slog_1 = list (filter( lambda i: i == "а" or i == "у" or i == "е" or i == "ы" or i == "о" or i == "э" or i == "я" or i == "и" or i == "ю" ,string_11))
slog_2 = list (filter( lambda i: i == "а" or i == "у" or i == "е" or i == "ы" or i == "о" or i == "э" or i == "я" or i == "и" or i == "ю" ,string_22))
slog_3 = list (filter( lambda i: i == "а" or i == "у" or i == "е" or i == "ы" or i == "о" or i == "э" or i == "я" or i == "и" or i == "ю" ,string_33))

if len(slog_1) == len (slog_2) == len(slog_3):
    print ("Парам пам-пам")
else:
    print ("Пам парам")


