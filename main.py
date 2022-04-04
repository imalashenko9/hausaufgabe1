
#1
def count_vowels(text):
    vowels= 0
    if not (type(text) == str):
        return 42

    for i in text:
        if i in "aeiouAEIOU":
            vowels = vowels+1
    return vowels

text = ["kfkf","kfkf"]
print(count_vowels(text))

#2
def hamming(text1,text2):

    hamming_distance = 0
    for i, j in zip(text1,text2):
        if i != j: hamming_distance += 1
    if len(text1) == len(text2):
       return int(hamming_distance)
    else:
        return 0

text1 = "cat"
text2 = "kaa"
print(hamming(text1,text2))

#3
class Vehicle:
    def __init__(self, color, fuel_type):
        self.color = color
        self.fuel_type = fuel_type

class Car(Vehicle):
    def __init__(self, color, fuel_type,doors):
        super().__init__(color, fuel_type)
        self.doors = doors
    def __str__(self):
        return "Color: {0}, Fuel Type: {1}, Doors: {2}".format(self.color,self.fuel_type,self.doors)
class Bus(Vehicle):
    def __init__(self, color, fuel_type, passengers):
        super().__init__(color, fuel_type)
        self.passengers = passengers
    def __str__(self):
        return "Color: {0}, Fuel Type: {1}, Passengers: {2}".format(self.color,self.fuel_type,self.passengers)

car1 = Car("<color>", "<fuel_type>", "<doors>")
bus1 = Bus("<color>", "<fuel_type>", "<passengers>")
print(car1)
print(bus1)

#4
class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def print_book(self):
        print("{0},{1}".format(self.name,self.author))
book1 = Book("Dune","Frank Herbert")
book1.print_book()

#5
from collections import namedtuple
class BookShelf(object):
   def __init__(self):
       self.books = []
   def add_book_list(self,book):

           if isinstance(book, Book):

              self.books.append(book)

   def books_by_author(self,author):
       written_by_author = []
       for book in self.books:
           if book.author == author:
               written_by_author.append(book.name)
       return written_by_author
   def get_books(self):
       book_list = []
       for book in self.books:
           book_list.append(book.name)
       return book_list
   def clear_shelf(self):
       self.books.clear()
       return self.books

Book = namedtuple("Book","name,author")

n = BookShelf()
n.add_book_list(Book("Geometry", "Potter"))
n.add_book_list(Book("Math", "Harry"))
n.add_book_list(Book("English", "James Odd"))
o = n.books_by_author("Potter")
print(o)
g=n.get_books()
print(g)
c = n.clear_shelf()
print(c)

o = n.books_by_author("Potter")
print(o)
