#Создайте класс, описывающий книгу. Он должен содержать информацию об авторе, названии, годе издания и жанре.
#Создайте несколько разных книг. Определите для него операции проверки на равенство и неравенство,
#методы __repr__ и __str__.

class Book:

    def __init__(self, author, name, year, genre):
        self.author = author
        self.name = name
        self. year = year
        self. genre = genre

    def presentation (self):
        print(self.author, self.name, self. year, self. genre)

    def __str__(self):
        return("Autor", self.author,"Name", self.name, "Year of issue", self. year, "Genre", self. genre)

    def __repr__(self):
        return("Autor", self.author,"Name", self.name, "Year of issue", self. year, "Genre", self. genre)


book_1 = Book("Stephen King", "IT", 1968, "horrors")
book_2 = Book("Joanne Rowling", "harry potter box set: the complete collection", 2001, "fantasy")

book_1.presentation()
book_2.presentation()





