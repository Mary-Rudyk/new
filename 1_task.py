#Создайте класс, описывающий автомобиль. Создайте класс автосалона, содержащий в себе список
#автомобилей, доступных для продажи, и функцию продажи заданного автомобиля.

class Car:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def presentation (self):
        print("Car_list: name {} - price {}".format(self.name, self.price))


class Showroom:

    def sale(self):
       pass



car1 = Car("Opel", 1000)
car2 = Car("Mazda", 5000)

car1.presentation()
car2.presentation()

