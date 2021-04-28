#Напишите программу-калькулятор, которая поддерживает следующие операции: сложение, вычитание,
#умножение, деление и возведение в степень. Программа должна выдавать сообщения об ошибке и
#продолжать работу при вводе некорректных данных, делении на ноль и возведении нуля в
#отрицательную степень.


def summ(x, y):
    return x+y


def dif(x, y):
    return x-y


def mult(x, y):
    return x * y


def div(x, y):
    return x / y


def degr(x, y):
    return x ** y


def calc():

    while True:
        try:
            x = int(input("Write some X "))
            y = int(input("Write some Y "))
        except ValueError:
            print("Wrong type x or y")

        act = input("Write some action (+ - * / ^) ")

        if act == "+":
            print(summ(x, y))

        elif act == "-":
            print(dif(x, y))

        elif act == "*":
            print(mult(x, y))

        elif act == "/":
            try:
                print(div(x, y))
            except ZeroDivisionError as er:
                print(er)

        elif act == "^":
            try:
                print(degr(x, y))
            except ZeroDivisionError as er:
                print(er)


calc()



