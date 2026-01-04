#Activity-1
import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
polygon = turtle.Turtle()
num_sides = 6
side_length = 70
angle = 360.0/(num_sides)
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)
turtle.done()

#Activity-2
turtle.Screen().bgcolor("Aqua")
board = turtle.Turtle()
board.forward(100)
board.left(120)
board.forward(100)
board.left(120)
board.forward(100)
board.penup()
board.right(90)
board.forward(100)
board.right(12)
board.forward(100)
board.right(120)

#Python Data class
lst= ['apple', 'banana', 'cherry']
print('The original list is:', lst)
print('Length of the list:', len(lst))
print('The first element of the list:', lst[0])
print('The first element of the list:', lst[-1])

lst.append('kiwi')
print('The list after appending kiwi is:', lst)

# Activity-3
def test(lst1):
    result={}
    for item in lst1:
        result[item[0]]=item[1:]
    return result
    
student_list= [('John', 25,'York'), ('Jane', 30, 'Los Angeles'), ('Jack', 28, 'Boston')]
print(test(student_list))

#Activity: Class Person
class Person(object):
    def _init_(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(self.name, self.age)

class Employee(Person):
    def _init_(self,name,age,empid):
        self.empid = empid
        super()._init_(name, age)

a=Employee("janik", 34, 1001)
a.display()

#Activity 4: Parrot
class Parrot:
    species={"bird"}
    def _init_(self, name, age):
        self.name = name
        self.age = age

    def sing(self):
        print(f"{self.name} says squawk")
        print(f"{self.name} is a specie of {self.species}")

    def dance(self):
        print(f"{self.name} dances")

ames=Parrot("ames", 10)
whu=Parrot("whu", 14)

#Bot assignment
class robot:
    species="computer"
    def __init__(self, name, age):
        self.name = name
        self.age = age

tom=robot("tom", 15)
jerry=robot("jerry", 15)

#Library Class
class Library:
    def __init__(self, name):
        self.name = name
        self.books = ["Harry Potter", "Rich Dad Poor Dad", "Atomic Habits", "Python Basics"]
        self.lend_data = {}

    def display_books(self):
        print("\n📚 Available Books in the Library:")
        for book in self.books:
            print(f" - {book}")

    def lend_book(self, user, book):
        if book not in self.books:
            print(f"❌ The book '{book}' is not available.")
        elif book in self.lend_data:
            print(f"⚠️ Sorry, '{book}' is currently lent out.")
        else:
            self.lend_data[book] = user
            print(f"✅ Book '{book}' has been lent to {user}.")

    def add_book(self, book):
        if book in self.books:
            print("⚠️ This book already exists.")
        else:
            self.books.append(book)
            print(f"✅ Book '{book}' has been added.")

    def return_book(self, book):
        if book in self.lend_data:
            del self.lend_data[book]
            print(f"✅ Book '{book}' has been returned.")
        else:
            print(f"⚠️ '{book}' was not lent out.")

# --- Main Program Loop ---
if __name__ == "__main__":
    my_library = Library("City Central Library")
    while True:
        print("\n========== Library Menu ==========")
        print("1. Display Books\n2. Lend a Book\n3. Add a Book\n4. Return a Book\n5. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            my_library.display_books()
        elif choice == '2':
            user = input("Enter name: ")
            book = input("Enter book name: ")
            my_library.lend_book(user, book)
        elif choice == '3':
            book = input("Enter book to add: ")
            my_library.add_book(book)
        elif choice == '4':
            book = input("Enter book to return: ")
            my_library.return_book(book)
        elif choice == '5':
            break

# Inheritance Section
class Vehicle:
    def _init_(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class PersonObj(object):
    def _init_(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)

class EmployeeNew(PersonObj):
    def _init_(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
        super()._init_(name, idnumber)
