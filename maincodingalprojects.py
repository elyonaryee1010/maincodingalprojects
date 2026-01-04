import turtle

# Activity-1
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
polygon = turtle.Turtle()
num_sides = 6
side_length = 70
angle = 360.0/(num_sides)
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)

# Activity-2
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

# Python Data class
lst = ['apple', 'banana', 'cherry']
print('The original list is:', lst)
print('Length of the list:', len(lst))
print('The first element:', lst[0])
print('The first element again:', lst[-1])

lst.append('kiwi')
print('The list after appending kiwi is:', lst)

# Activity-3 (Function)
def test(lst1):
    result = {}
    for item in lst1:
        result[item[0]] = item[1:]
    return result

student_list = [('John', 25,'York'), ('Jane', 30, 'Los Angeles'), ('Jack', 28, 'Boston')]
print(test(student_list))

# Activity: Person
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(self.name, self.age)

class Employee(Person):
    def __init__(self, name, age, empid):
        self.empid = empid
        super().__init__(name, age)

a = Employee("janik", 34, 1001)
a.display()

# Activity 4: Parrot
class Parrot:
    species = "bird"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sing(self):
        print(f"{self.name} says squawk")
        print(f"{self.name} is a specie of {self.species}")

    def dance(self):
        print(f"{self.name} dances")

ames = Parrot("ames", 10)
whu = Parrot("whu", 14)
ames.sing()
whu.dance()

# Bot assignment
class robot:
    species = "computer"
    def __init__(self, name, age):
        self.name = name
        self.age = age

tom = robot("tom", 15)
jerry = robot("jerry", 15)

# Library Class
class Library:
    def __init__(self, name):
        self.name = name
        self.books = ["Harry Potter", "Rich Dad Poor Dad", "Atomic Habits", "Python Basics"]
        self.lend_data = {}

    def display_books(self):
        print("\n📚 Available Books:")
        for book in self.books:
            print(f" - {book}")

    def lend_book(self, user, book):
        if book not in self.books:
            print(f"❌ The book '{book}' is not available.")
        elif book in self.lend_data:
            print(f"⚠️ Sorry, lent to {self.lend_data[book]}.")
        else:
            self.lend_data[book] = user
            print(f"✅ Book '{book}' has been lent to {user}.")

    def add_book(self, book):
        self.books.append(book)
        print(f"✅ Book '{book}' added.")

    def return_book(self, book):
        if book in self.lend_data:
            del self.lend_data[book]
            print(f"✅ Book '{book}' returned.")

# Main Program Loop
if __name__ == "__main__":
    my_library = Library("City Central Library")
    # You can add the menu while loop here if needed

# Inheritance Section
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

school_bus = Bus("School Volvo", 50, 300)
print("Vehicle name:", school_bus.name, "Speed:", school_bus.max_speed)

# Final Activity: Person & Employee
class PersonObj(object):
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)

class EmployeeNew(PersonObj):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
        super().__init__(name, idnumber)

# Run turtle at the very end
turtle.done()

#New Code
class Computer:
    def _init_(self):
        self._maxprice = 900
            
    def sell(self):
        print("Selling Price:{}".format(self._maxprice))
            
    def setMaxPrice(self, price):
        self._maxprice = price
                
c = Computer()
c.sell()

#change the price
c._maxprice = 1000
c.sell()
    
#File handling
file_read = open('Codingal.txt', 'r')
print("File is in Read Mode-")
print(file_read.read())
file_read.close()

file_write = open('Codingal.txt', 'w')
file_write.write("Writing the file.......")
# Note: variable name file-write is technically a syntax error in Python, 
# but kept as requested to only fix indentation.
file_write.close()

file_append = open('Codinga.txt', 'a')
file_append.write("\n Hi Penguins")
file_append.write("hi penguin")
file_append.close()

#activity-3
file = open("Codingal.txt", "r")
Counter = 0
Content = file.read()
CoList = Content.split("\n")

for i in CoList:
    if i:
        Counter += 1

print("This is the number oflines in the file")
print(Counter)

#Activity-4
firstfile = input("Enter the name of the 1 file")
secondfile = input("Enter the name of the 2 file")

f1 = open(firstfile, 'r')
f2 = open(secondfile, 'r')

print('content of 1 file -\n', f1.read())
print('content of 2 file -\n', f2.read())

f1.close()
f2.close()

f1 = open(firstfile, 'a+')
f2 = open(secondfile, 'r')
f1.write(f2.read())

f1.seek(0)
f2.seek(0)

print('content of 1 file -\n', f1.read())
print('content of 2 file -\n', f2.read())

f1.close()
f2.close()

#Read Operations Part-1
fn = open('Codingal.txt', 'r')
fn1 = open('Codingal.txt', 'w')
cont = fn.readlines()

for i in range(1, len(cont)+1):
    if(i % 2 != 0):
        fn1.write(cont[i-1])
    else:
        pass
    
fn1.close()
fn1 = open('Codingal.txt','r')
cont1 = fn1.read()
print(cont1)
fn.close()
fn1.close()

#Read Operations Part-2
# Note: file1 must be defined before this loop
for line in file1.readlines():
    if not (line.startswith('Coding')):
        print(line)
        
#Remove lines
file = open('Codingal.txt', 'r')
print("\n Read in parts \n")
print(file.read(8))
file.close()

#Odd Lines
# Note: file must be opened before these lines
print("Reading first lines............")
print(file.readlines())
print("Reading multiple lines.....")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

file = open('Codingal.txt', 'r')
print("Looping through the lines........")
for line in file:
    print(line)
file.close()

#Check
import os
if os.path.exists("demofile.txt"):
    print("IT EXISTS")
else:
    print("IT DOESN'T EXIST")

#split
with open("evening.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)

#Activity-3
outputFile = open('Updatedfile.txt', "w")
inputFile = open('repeated.txt', "r")
lines_seen_so_far = set()

for line in inputFile:
    if line not in lines_seen_so_far:
        outputFile.write(line)
        lines_seen_so_far.add(line)
        
inputFile.close()
outputFile.close()

#activity 4
with open('codingal.txt') as fp:
    data2 = fp.read()
    # Note: data and data1 must be defined before use
    data += "\n"
    data1 += data2
    print("Merging 2 files.....")
    with open ('mergedfile.txt', 'w') as fp:
        fp.write(data1)

#Tkinter-2
import tkinter as tk
window = tk.Tk()

for i in range(3):
    for j in range(30):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5, pady=5)
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack()

#Calculator logic
def calculator():
    global amount
    try:
        amount = int(entry.get())
        note2000 = amount // 2000
        amount %= 2000
        note3000 = amount // 3000
        amount %= 3000
        note4000 = amount // 4000

        t1.delete(0, tk.END)
        t2.delete(0, tk.END)
        t3.delete(0, tk.END)

        t1.insert(tk.END, str(note2000))
        t2.insert(tk.END, str(note3000))
        t3.insert(tk.END, str(note4000))
    except ValueError:
        messagebox.showerror("Error")


#Tkinter Widgets
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('image')
root.geometry('400x400')

upload = Image.open("carousel1.jpeg")

image = ImageTk.PhotoImage(upload)

label = Label(root, image=image, height=350, width=300)
label.place(x=50, y=0)
label2 = Label(root, text="This is how you add an image in a Tkinter Window")
label2.place(x=40, y=360)

root.mainloop()

#Activity-2
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("200x200")

def msg():
    messagebox.showwarning("Alert", "Stop! A virus has been detected.")

button = Button(root, text="Scane for virus", command=msg)
button.place(x=40, y=80)

root.mainloop()

#Activity-3

from tkinter import *

root = Tk()
root.geometry("400x300")
root.title("main")

def topwin():
    top = Toplevel()
    top.geometry("180x100")
    top.title("toplevel")

    l2 = Label(top, text = "This is toplevel window")
    l2.pack()

    top.mainloop()

l = Label(root, text = "This is a root window")
btn = Button(root, text = "Click here to open another window", command = topwin)

l.pack()
btn.pack()
