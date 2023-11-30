# -*- coding: utf-8 -*-
"""python_practice_5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aM-P_YvTh23scmKfAnanxr3HRemm4Tbp

# I. OOP

1. (7б). Створіть клас Animal, додайте docstring, три атрибути, один з яких має значення за замовчуванням та два методи на свій розсуд.
"""

class Animal:
   def __init__(self,name, age, sound = 'Bark'):
      self.name = name
      self.age = age
      self.sound = sound
   def make_sound(self):
      return f"{self.name} is a dog and can {self.sound}"
   def give_info(self):
      return f"Dog's name is {self.name} and he/she is {self.age} y.o."

"""1.1. (5б). Створіть два обʼєкти цього класу. На одному обʼєкті отримайте значення його атрибуту, а на іншому викличте один з його методів."""

dog_one = Animal("Django", 10)
print(dog_one.name, dog_one.age)

dog_two = Animal("Vilulu" , 12)
dog_two.give_info()

"""2. (9б). Створіть клас, де атрибути мають різні рівні доступу. Спробуйте отримати їхні значення та опишіть результати."""

class private_public_print:
  def public(self):
    print("Public method")
  def __private(self):
    print("Private method")

showcase_one = private_public_print()
print(showcase_one.public())
print(showcase_one.__private())

"""3. (8б). Як ви розумієте термін self? Для чого використовується метод __init __?

*місце для відповіді*

4. (8б). Створіть клас Фігура без атрибутів, з методом get_area для отримання площі фігури, що повертає 0 та __add __, який приймає self та other в якості аргументів, а повертає суму площин фігур self та other.
"""

class Figure:
  def get_area():
    return 0
  def __add__(self,other):
    return self.get_area() + other.get_area()

"""5. (11б). Створіть 2 дочірніх класи від Фігури: Трикутник та Коло, які мають атрибути, необхідні для розрахунку площин. Визначте метод get_area в кожному з них так, щоби вони розраховували площу в залежності від формули для кожного типу фігури. Створіть обʼєкт класу Трикутник та обʼєкт класу Коло. Виконайте операцію суми за допомогою оператора + між ними."""

class Triangle(Figure):
  def __init__ (self, height, base):
    self.height = height
    self.base = base
  def get_area(self):
    return 0.5 * (self.base * self.height)

class Circle(Figure):
  def __init__ (self, radius):
    self.radius = radius
  def get_area(self):
    return 3.14 * (self.radius ** 2)

Triangle_one = Triangle(10,5)
Triangle_one.get_area()
Circle_one = Circle(5)
Circle_one.get_area()
total_area = Circle_one + Triangle_one
print(total_area)

"""6. (7б). Продемонструйте різницю між isinstance та issubclass."""

example_isinstance = isinstance(5,int)
print(example_isinstance)
#checks if an object is of the specified type

example_issubclass = issubclass(Triangle, Figure)
print(example_issubclass)
#checks if the object is a subclass of the specified object

"""7. (16б). Створіть клас BankAccount з приватними атрибутами balance та account_number.
Реалізуйте методи поповнення та зняття коштів, забезпечивши належну інкапсуляцію. Підказка: використовуйте декоратори getter та setter.
"""

class BankAccount:
    def __init__(self, account_number):
        self._balance = 0
        self._account_number = account_number

    def get_balance(self):
        return self._balance

    def set_balance(self, amount):
        if amount < 0:
            print("Amount must be non-negative.")
        else:
            self._balance = amount
            print(f"Balance updated: {self._balance}")

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited {amount}. New balance: {self._balance}")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew {amount}. New balance: {self._balance}")
        elif amount > self._balance:
            print("Insufficient funds.")
        else:
            print("Withdrawal amount must be greater than zero.")

    def get_account_number(self):
        return self._account_number


account = BankAccount("57377")
print("Account Number:", account.get_account_number())
account.set_balance(3356)
print("Current Balance:", account.get_balance())

account.withdraw(777)
account.deposit(6969)

"""8. (16б). Створіть клас Library, який містить список об'єктів типу Book.
Реалізуйте методи для додавання книги, видалення книги та відображення списку книг.
"""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
            print(f"Added {book.title} to the library.")
        else:
            print("Invalid book object. Please add a valid Book instance.")

    def display_books(self):
        if self.books:
            print("Books available in the library:")
            for book in self.books:
                print(book)
        else:
            print("The library is empty. No books available.")


library = Library()

book1 = Book("Harry Potter and the Deathly Hallows", "J.K. Rowling")
book2 = Book("Da Vinci Code,The", "	Brown, Dan")

library.add_book(book1)
library.add_book(book2)
library.display_books()

"""9. (13б). Створіть клас Person з атрибутами name та age.
Створіть ще один клас Employee з такими атрибутами, як department та salary.
Створіть клас Manager, який успадковує обидва класи Person та Employee. Продемонструйте використання множинної спадковості, створивши обʼєкт класу Manager та отримавши mro для цього класу.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee:
    def __init__(self, department, salary):
        self.department = department
        self.salary = salary


class Manager(Person, Employee):
    def __init__(self, name, age, department, salary):
        Person.__init__(self, name, age)
        Employee.__init__(self, department, salary)

    def __str__(self):
        return f"Manager: {self.name}, Age: {self.age}, Department: {self.department}, Salary: {self.salary}$"

manager = Manager("John Doe", 40, "IT", 60000)
print(manager)

print("Method Resolution Order (MRO) for Manager:")
print(Manager.mro())

"""# Вітаю! Ви велика(ий) молодець, що впоралась(вся). Похваліть себе та побалуйте чимось приємним. Я Вами пишаюся."""