class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    pass

dog = Dog()
dog.eat()

class Payable:
    def pay(self):
        pass

class Payment(Payable):
    def pay(self):
        print("Payment completed")

payment = Payment()
payment.pay()

class Room:
    def show(self):
        print("This is a room")

class House:
    def __init__(self):
        self.room = Room()

house = House()
house.room.show()

class Book:
    def show(self):
        print("This is a book")

class Library:
    def __init__(self, book):
        self.book = book

book = Book()
library = Library(book)
library.book.show()

class Order:
    def show(self):
        print("Customer has an order")

class Customer:
    def __init__(self, order):
        self.order = order

order = Order()
customer = Customer(order)
customer.order.show()

class Document:
    def print_document(self):
        print("Printing document")

class Printer:
    def print_file(self, document):
        document.print_document()

document = Document()
printer = Printer()

printer.print_file(document)