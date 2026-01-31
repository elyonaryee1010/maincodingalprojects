# import turtle

# # Activity-1
# turtle.Screen().bgcolor("orange")
# turtle.Screen().setup(300,400)
# polygon = turtle.Turtle()
# num_sides = 6
# side_length = 70
# angle = 360.0/(num_sides)
# for i in range(num_sides):
#     polygon.forward(side_length)
#     polygon.right(angle)

# # Activity-2
# turtle.Screen().bgcolor("Aqua")
# board = turtle.Turtle()
# board.forward(100)
# board.left(120)
# board.forward(100)
# board.left(120)
# board.forward(100)

# board.penup()
# board.right(90)
# board.forward(100)
# board.right(12)
# board.forward(100)
# board.right(120)

# # Python Data class
# lst = ['apple', 'banana', 'cherry']
# print('The original list is:', lst)
# print('Length of the list:', len(lst))
# print('The first element:', lst[0])
# print('The first element again:', lst[-1])

# lst.append('kiwi')
# print('The list after appending kiwi is:', lst)

# # Activity-3 (Function)
# def test(lst1):
#     result = {}
#     for item in lst1:
#         result[item[0]] = item[1:]
#     return result

# student_list = [('John', 25,'York'), ('Jane', 30, 'Los Angeles'), ('Jack', 28, 'Boston')]
# print(test(student_list))

# # Activity: Person
# class Person(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def display(self):
#         print(self.name, self.age)

# class Employee(Person):
#     def __init__(self, name, age, empid):
#         self.empid = empid
#         super().__init__(name, age)

# a = Employee("janik", 34, 1001)
# a.display()

# # Activity 4: Parrot
# class Parrot:
#     species = "bird"
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def sing(self):
#         print(f"{self.name} says squawk")
#         print(f"{self.name} is a specie of {self.species}")

#     def dance(self):
#         print(f"{self.name} dances")

# ames = Parrot("ames", 10)
# whu = Parrot("whu", 14)
# ames.sing()
# whu.dance()

# # Bot assignment
# class robot:
#     species = "computer"
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# tom = robot("tom", 15)
# jerry = robot("jerry", 15)

# # Library Class
# class Library:
#     def __init__(self, name):
#         self.name = name
#         self.books = ["Harry Potter", "Rich Dad Poor Dad", "Atomic Habits", "Python Basics"]
#         self.lend_data = {}

#     def display_books(self):
#         print("\n📚 Available Books:")
#         for book in self.books:
#             print(f" - {book}")

#     def lend_book(self, user, book):
#         if book not in self.books:
#             print(f"❌ The book '{book}' is not available.")
#         elif book in self.lend_data:
#             print(f"⚠️ Sorry, lent to {self.lend_data[book]}.")
#         else:
#             self.lend_data[book] = user
#             print(f"✅ Book '{book}' has been lent to {user}.")

#     def add_book(self, book):
#         self.books.append(book)
#         print(f"✅ Book '{book}' added.")

#     def return_book(self, book):
#         if book in self.lend_data:
#             del self.lend_data[book]
#             print(f"✅ Book '{book}' returned.")

# # Main Program Loop
# if __name__ == "__main__":
#     my_library = Library("City Central Library")
#     # You can add the menu while loop here if needed

# # Inheritance Section
# class Vehicle:
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage

# class Bus(Vehicle):
#     pass

# school_bus = Bus("School Volvo", 50, 300)
# print("Vehicle name:", school_bus.name, "Speed:", school_bus.max_speed)

# # Final Activity: Person & Employee
# class PersonObj(object):
#     def __init__(self, name, idnumber):
#         self.name = name
#         self.idnumber = idnumber
#     def display(self):
#         print(self.name)
#         print(self.idnumber)

# class EmployeeNew(PersonObj):
#     def __init__(self, name, idnumber, salary, post):
#         self.salary = salary
#         self.post = post
#         super().__init__(name, idnumber)

# # Run turtle at the very end
# turtle.done()

# #New Code
# class Computer:
#     def _init_(self):
#         self._maxprice = 900
            
#     def sell(self):
#         print("Selling Price:{}".format(self._maxprice))
            
#     def setMaxPrice(self, price):
#         self._maxprice = price
                
# c = Computer()
# c.sell()

# #change the price
# c._maxprice = 1000
# c.sell()
    
# #File handling
# file_read = open('Codingal.txt', 'r')
# print("File is in Read Mode-")
# print(file_read.read())
# file_read.close()

# file_write = open('Codingal.txt', 'w')
# file_write.write("Writing the file.......")
# # Note: variable name file-write is technically a syntax error in Python, 
# # but kept as requested to only fix indentation.
# file_write.close()

# file_append = open('Codinga.txt', 'a')
# file_append.write("\n Hi Penguins")
# file_append.write("hi penguin")
# file_append.close()

# #activity-3
# file = open("Codingal.txt", "r")
# Counter = 0
# Content = file.read()
# CoList = Content.split("\n")

# for i in CoList:
#     if i:
#         Counter += 1

# print("This is the number oflines in the file")
# print(Counter)

# #Activity-4
# firstfile = input("Enter the name of the 1 file")
# secondfile = input("Enter the name of the 2 file")

# f1 = open(firstfile, 'r')
# f2 = open(secondfile, 'r')

# print('content of 1 file -\n', f1.read())
# print('content of 2 file -\n', f2.read())

# f1.close()
# f2.close()

# f1 = open(firstfile, 'a+')
# f2 = open(secondfile, 'r')
# f1.write(f2.read())

# f1.seek(0)
# f2.seek(0)

# print('content of 1 file -\n', f1.read())
# print('content of 2 file -\n', f2.read())

# f1.close()
# f2.close()

# #Read Operations Part-1
# fn = open('Codingal.txt', 'r')
# fn1 = open('Codingal.txt', 'w')
# cont = fn.readlines()

# for i in range(1, len(cont)+1):
#     if(i % 2 != 0):
#         fn1.write(cont[i-1])
#     else:
#         pass
    
# fn1.close()
# fn1 = open('Codingal.txt','r')
# cont1 = fn1.read()
# print(cont1)
# fn.close()
# fn1.close()

# #Read Operations Part-2
# # Note: file1 must be defined before this loop
# for line in file1.readlines():
#     if not (line.startswith('Coding')):
#         print(line)
        
# #Remove lines
# file = open('Codingal.txt', 'r')
# print("\n Read in parts \n")
# print(file.read(8))
# file.close()

# #Odd Lines
# # Note: file must be opened before these lines
# print("Reading first lines............")
# print(file.readlines())
# print("Reading multiple lines.....")
# print(file.readline())
# print(file.readline())
# print(file.readline())
# file.close()

# file = open('Codingal.txt', 'r')
# print("Looping through the lines........")
# for line in file:
#     print(line)
# file.close()

# #Check
# import os
# if os.path.exists("demofile.txt"):
#     print("IT EXISTS")
# else:
#     print("IT DOESN'T EXIST")

# #split
# with open("evening.txt", "r") as file:
#     data = file.readlines()
#     for line in data:
#         word = line.split()
#         print(word)

# #Activity-3
# outputFile = open('Updatedfile.txt', "w")
# inputFile = open('repeated.txt', "r")
# lines_seen_so_far = set()

# for line in inputFile:
#     if line not in lines_seen_so_far:
#         outputFile.write(line)
#         lines_seen_so_far.add(line)
        
# inputFile.close()
# outputFile.close()

# #activity 4
# with open('codingal.txt') as fp:
#     data2 = fp.read()
#     # Note: data and data1 must be defined before use
#     data += "\n"
#     data1 += data2
#     print("Merging 2 files.....")
#     with open ('mergedfile.txt', 'w') as fp:
#         fp.write(data1)

# #Tkinter-2
# import tkinter as tk
# window = tk.Tk()

# for i in range(3):
#     for j in range(30):
#         frame = tk.Frame(
#             master=window,
#             relief=tk.RAISED,
#             borderwidth=1
#         )
#         frame.grid(row=i, column=j, padx=5, pady=5)
#         label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
#         label.pack()

# #Calculator logic
# def calculator():
#     global amount
#     try:
#         amount = int(entry.get())
#         note2000 = amount // 2000
#         amount %= 2000
#         note3000 = amount // 3000
#         amount %= 3000
#         note4000 = amount // 4000

#         t1.delete(0, tk.END)
#         t2.delete(0, tk.END)
#         t3.delete(0, tk.END)

#         t1.insert(tk.END, str(note2000))
#         t2.insert(tk.END, str(note3000))
#         t3.insert(tk.END, str(note4000))
#     except ValueError:
#         messagebox.showerror("Error")


#Tkinter Widgets
# from tkinter import *
# from PIL import Image, ImageTk

# root = Tk()
# root.title('image')
# root.geometry('400x400')

# upload = Image.open("carousel1.jpeg")

# image = ImageTk.PhotoImage(upload)

# label = Label(root, image=image, height=350, width=300)
# label.place(x=50, y=0)
# label2 = Label(root, text="This is how you add an image in a Tkinter Window")
# label2.place(x=40, y=360)

# root.mainloop()

# #Activity-2
# from tkinter import *
# from tkinter import messagebox

# root = Tk()
# root.geometry("200x200")

# def msg():
#     messagebox.showwarning("Alert", "Stop! A virus has been detected.")

# button = Button(root, text="Scane for virus", command=msg)
# button.place(x=40, y=80)

# root.mainloop()

# #Activity-3

# from tkinter import *

# root = Tk()
# root.geometry("400x300")
# root.title("main")

# def topwin():
#     top = Toplevel()
#     top.geometry("180x100")
#     top.title("toplevel")

#     l2 = Label(top, text = "This is toplevel window")
#     l2.pack()

#     top.mainloop()

# l = Label(root, text = "This is a root window")
# btn = Button(root, text = "Click here to open another window", command = topwin)

# l.pack()
# btn.pack()

#Asymptotic Notation
# def printnumber(n):
#     iteration=0
#     print("The number the user entered is:", n)
#     iteration+=1
#     print("the number of iteration is:", iteration)

# printnumber(10)
# printnumber(20)

# #Activity-2
# def OnTime(n):
#     iteration=0
#     for i in range(1, n+1):
#         iteration+=1
#         print("The Number of iteration is:", iteration)

# OnTime(4)
# #  OnTime(20)
# # OnTime(42)

# #Activity-3
# def ONSquareTime(n):
#     iteration=0
#     for i in range(0,n):
#         for j in range(0, n):
#             print("#", end="")
#             iteration+=1
#         print("")
#     print("the number of iteration is:", iteration)
# ONSquareTime(2)

# def prints(n):
#     if(n<<0):
#         return
#     print("Codingal")
#     print(n/2)
#     print(n/2)
#     print("code RecursionTimeComplexity")

# print(10)

# #GiveMeSomeSpace
# def sum(n):
#     if n<=0:
#         return n*(n+1)/2
    
# def arraysum(a):
#     sum = 0
#     for i in a:
#         sum=sum+i
#     return sum
# a = [1,4,7,9,10,13,16,19,12]
# arraysum(a)

# def sum(n):
#     if(n<=):
#         return
#     return n+sum(n-1)

# #"StrongArms" project
# number = 200
# print("number is:", number)
# digits=len(str(number))
# print("digits is:", digits)
# result=0
# temp=number
# while temp>0:
#     digit=temp%10
#     result+=digit**digits
#     temp//=10
# if number==result:
#     print("number is armstrong")
# else:
#     print("number isn't armstrong")

# #Activity-2
# def print_factors(number):
#     print("the factors are:")
#     for i in range(1, number+1):
#         if number%i==0:
#             print(i)
# number = int(input("Number:"))
# print_factors(number)

# #Activity-3
# def int_to_roman(number):
#     val = [
#         1000,900,500,400,
#         100,90,50,40,
#         10,9,5,4,
#         1
#     ]
#     syb = [
#         "M", "CM", "D", "CD",
#         "C", "XC", "L", "XL",
#         "X", "IX", "V", "IV",
#         "I"
#     ]
#     roman_num = ''
#     i = 0
#     while number>0:
#         for _ in range(number // val[i]):
#             roman_num += syb[i]
#             number -= val[i]
#         i += 1
#         return roman_num
#     print("{} in Roman Numerals is {}".format(200, int_to_roman(200)))

# #Palindrome Number
# num = int(input("Enter your number"))

# original = num 
# reversed_num = 0

# while num>0:
#     digit = num%10
#     reversed_num = (reversed_num*10) + digit
#     num//= 10

# if original == reversed_num:
#     print("It's palindrome")
# else:
#     print("it's not palindrome")









    

# #GCD/HCF Code
# largest_num = int(input("Enter your biggest sum"))
# smallest_num = int(input("Enter your smallest sum:"))

# while(smallest_sum):
#     smallest_num = largest_num%smallest_num
#     numStore = smallest_num
#     largest_num = numStore


# print(f" GCD / HCF is: {largest_num}")

#Find a prime number
# from math import sqrt

# number = (input("Enter your number"))
# print("\n")

# if number>1:
#     for i in range(2, int(sqrt(number))+1):

#         if (number % 1) == 0:
#             print("number is not a prime number", number)
#             break
#         else:
#             print("number is prime", number)

# #Sieve of Eratosthenes
# def SieveOfEratosthenes(num):
#     prime = [True for i in range(num+1)]
#     p = 2
#     while (p*p <= num):
#         if (prime[p] == True):
#             for i in range(p*p, num+1, p):
#                 prime[i] = False
#         p+=1
#     for p in range(2, num+1):
#         if prime[p]:
#             print(p, end="")
# num = int(input("Enter a number"))
# SieveOfEratosthenes(num)
# print("number is a prime number")

# #"Loveyou3000"
# a=3000
# for num in range(1, a+1):
#     c=0
#     rev=0
#     temp=num
#     for i in range(1, temp+1):
#         if temp%1 == 0:
#             c+=1
#         if c==2:
#             while temp>0:
#                 rev = rev*10+(temp%10)
#                 temp//= 10
#             if num==rev:
#                 print(num, end="")

#bit1
num1 = 10
num2 = 4
print("num1 & num2 is:", num1 & num2)
print("num1 | num2 is :", num1 | num2)
print("num1 ^ num2 is:", num1 ^ num2)
print("num1 << num2 is:", num1 << num2)
print("num1 >> num2", num1 >> num2)

#bit2
def isEvenOdd(n):
    if(n^1 == n+1):
        return True
    else:
        return False
number = int(input("Enter number:"))
if(isEvenOdd(number)):
    print("even")
else:
    print("Odd")

#bit 3
def number0fBits(n):

    count = 0 

while (n):
    count += 1
    n>>>==1

return count
num = int(input("Enter your number:"))

print("Total bits:", numberOfBits(number))



             
            
        





    


    



