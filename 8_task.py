#Создайте иерархию классов транспортных средств. В общем классе опишите общие для всех
#транспортных средств поля, в наследниках – специфичные для них. Создайте несколько экземпляров.
#Выведите информацию о каждом транспортном средстве.

class Car:
    def __init__(self):
        self.name = "Auto"
        self.number_wheels = 4
        self.number_seats = 5
        print("Name: ", self.name,"Number of wheels: ", self.number_wheels, "Number of seats: ", self.number_seats)


class Small(Car):
    def __init__(self):
        super().__init__()
        self.engine_volume = 1.8
        self.car_brend = "Opel"
        self.color = "Red"
        print("Car brend: ", self.car_brend, "Color: ", self.color, "engine_volume: ", self.engine_volume)
        print()


class Big(Car):
    def __init__(self):
        super().__init__()
        self.car_brend = "Mazda"
        self.color = "Blue"
        self.engine_volume = 2.5
        print("Car brend: ", self.car_brend, "Color: ", self.color, "engine_volume: ", self.engine_volume)
        print()


def main():
    car1 = Small()
    car2 = Big()


main()




