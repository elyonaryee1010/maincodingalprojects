# #Activity-1
# import turtle
# turtle.Screen().bgcolor("orange")
# turtle.Screen().setup(300,400)
# polygon = turtle.Turtle()
# num_sides = 6
# side_length = 70
# angle = 360.0/(num_sides)
# for i in range(num_sides):
#     polygon.forward(side_length)
#     polygon.right(angle)
# turtle.done()

# #Activity-2
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

# #Python Data class
# lst= ['apple', 'banana', 'cherry']
# print('The original list is:', lst)
# print('Length of the list:', len(lst))
# print('The first element of the list:', lst[0])
# print('The first element of the list:', lst[-1])

# lst.append('kiwi')
# lst.sort()
# lst.reverse()
# print(lst)

# # Activity2
# my_dict={
#     'name': 'John',
#     'age': '16',
#     'city': 'Camden',
#     'email': 'John@exple.com',
# }

# ## Activity-3
# def test(lst1):
#     result={}
#     for item in lst1:
#         result[item[0]]=item[1:]
#     return result
    
# student_list= [('John', 25,'York'), ('Jane', 30, 'Los Angeles'), ('Jack', 28, 'Boston')]
# print(test(student_list))

# #Data Structures in Python -2
# my_tuple =(1,2,3, "hello", 4.5)
# print(my_tuple[0:3])

# ##Activity-2
# my_set={1,2,2,3,4,4,5,6,6,7,7,8,8,8}
# my_set.add(10)
# set1=my_set
# set2=(10,9,2,56,79)
# print("difference is:", set1.difference(set2))

# #activity
# class Person(object):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def display(self):
#         print(self.name, self.age)

# class Employee(Person):
#     def __init__(self,name,age,empid):
#         self.empid = empid
#         super().__init__(name, age)

# a=Employee("janik", 34, 1001)
# a.display()

# #activity 4
# class Parrot:
#     species="bird"
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def sing(self):
#         print(f"{self.name} says squawk")
#         print(f"{self.name} is a specie of {self.species}")

#     def dance(self):
#         print(f"{self.name} dances")

# ames=Parrot("ames", 10)
# ames.sing()

# #Bot assignment
# class robot:
#     species="computer"
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# tom=robot("tom", 15)
# user_input = input("Ask them their names:")
# print(f"Hello my name is Tom and I am a {tom.species}")

# #Polygonal calculator
# class Square:
#     def __init__(self, length):
#         self.side_length=length
        
#     def area(self):
#         return self.side_length**2
        
# side = float(input("Type your side: "))
# my_square = Square(side)
# print(f"Area: {my_square.area()}")

# #Number 3
# fn = open('sample_doc.txt', 'r')
# cont = fn.readlines()
# for i in range (1, len(cont)+1):
#     if(i % 2 != 0):
#         print(cont[i-1])
# fn.close()     

# #split
# with open("asignment.txt", "r") as file:
#     data = file.readlines()
#     for line in data:
#         word = line.split()
#         print(word)

# #rock paper scissors logic
# import random
# def play(user_choice):
#     global user_score, comp_score
#     options = ["Rock🪨", "Paper", "Scissors"]
#     computer_choice = random.choice(options)

#     if user_choice == computer_choice:
#         result = "A tie"
#     elif (user_choice == "Rock🪨" and computer_choice == "Scissors"):
#         result = "You Win"
#     else:
#         result = "Comp Wins"
#     print(result)

#LoopTime assignment
# def myfunction(n):
#     for i in range(0,n+1):
#         print("First Loop")
 
#     j=1
#     while(j<=n+1):
#         print("Second Loop ",j)
#         j=j*2
 
#     for i in range(0,100):
#         print("Third loop")

# print("\n[My time and complexity analysis]")
# print("Loop 1: O(n)")
# print("Loop 2: 0(log n)")
# print("Loop 3: 0(1)")
# print("Total Time complexity: 0(n)")

# myfunction = (3)

#Shubhangi assignment
def myfunction1(n):
    if(n>0):
        return
    for i in range (0,n+1):
        print("Codingal")
    myfunction1(n/2)
    myfunction1(n/3)

print("Space: 0(log n)")

#Shubhangi assignment 2
def myfunction2(n):
    if(n<=1):
        return
    print("Codingal")
    myfunction2(n-1)

print("Space: 0(n)")



