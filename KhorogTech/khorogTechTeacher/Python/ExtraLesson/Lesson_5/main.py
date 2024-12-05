
#! Напишите программу, которая проверяет, какой день недели сегодня. Если это понедельник, выведите "Начало недели", если пятница, выведите "Почти выходные", а если выходные (суббота или воскресенье), выведите "Выходные".

# day = input("chedom ruz")
# if day == "monday":
#     print("Nachalo nedeli")
# elif day == "friday":
#     print("Konec nededli")
# elif day == "saturday" or day == "sanday":
#     print("Odix")
# else:
#     print("Dizga")
    
#! Напишите программу, которая запрашивает у пользователя время в часах (0-23) и выводит, является ли это время "Утро" (0-11), "День" (12-17) или "Вечер" (18-23).
def Time_of_day():
    hour = int(input("sowat conde"))
    if hour >= 0 and hour <= 11:
        print("Utro")
    elif hour >= 12 and hour <= 17:
        print("Den")
    elif hour >=18 and hour <=23:
        print("Vecher")
    else:
        print("Dizga soate nist")
Time_of_day()


#! Определение класса книги
#! Напишите программу, которая принимает возраст пользователя и тип книги (художественная, научная, учебная) и выводит рекомендацию, подходит ли эта книга для данного возраста. Используйте if, else, и elif.
# age = int (input("tut cond sola"))
# book_type = input("Введите тип книги (художественная, научная, учебная")
# if book_type == "художественная":
#     if age <12:
#         print("Nest munkin culikenard")
#     elif age <=18:
#         print("Munkin ghulayenar")
#     else:
#         print("Ghulayenard munkin mis")
# elif book_type == "научная":
#     if age <12:
#         print("Nest munkin culikenard")
#     elif age <=18:
#         print("Munkin ghulayenar")
#     else:
#         print("Ghulayenard munkin mis")
# elif book_type == "учебная":
#     if age <12:
#         print("Munkin") 
#     else:
#         print("Fukathard podkhodit kixt")
# else:
#     print("Dezga kitob nist")


# GetNumber()
# parametri a, b,c,d,
# argument a1 , b1 , c1, d1
# f = a +b *(c-d)

a1 = int(input("a1 cond"))
b1 = int(input("b1 cond"))
c1 = int(input("c1 cond"))
d1 = int(input("d1 cond"))
def GetNumber(a,b,c,d):
    f = a  +b * (c-d)
    print(f)

GetNumber(a1, b1, c1, d1)