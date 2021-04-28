#Опишите свой класс исключения. Напишите функцию, которая будет выбрасывать данное исключение,
#если пользователь введёт определённое значение, и перехватите это исключение при вызове функции.

class MyExcepError (Exception):
    pass


def positive():
    while True:
        number = float(input("Write some  positive number "))
        if number >= 0:
            result = number ** 0.5
            print(result)
        elif number < 0:
            raise MyExcepError("My error")



positive()



