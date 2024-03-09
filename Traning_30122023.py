##Anonymous Functions
##Lambda Function
# add=lambda x,y: x+y
# print(add(30,40))

## Find Even Odd number with User input
# x=int(input("Enter the Number:" ))
# even_odd=lambda x: "Even" if x%2==0 else "odd"
# print(even_odd(x))

## Python Variable Scope
##Local Variable:
# def greet():
#     #lacal Variable
#     message='Hello'
#     print('Local',message)
# greet()
##Try to access message variable
##outside greet() function
## Global Variale:
# message='Hello'
# def greet1():
#     #lacal Variable
    
#     print('Global',message)
# greet1()
# print(message)

####Special Functions: "Filter" "Map" "Reduce"
### Filter:
# list1=[1,2,3,4,5,6,7,8,9]
# even=lambda x: x%2==0
# even_list=list(filter(even,list1))
# print(even_list)
# odd=lambda s: s%2!=0
# odd_list=list(filter(odd,list1))
# print(odd_list)

### Map:
# list2=[1,2,3,4,5,6,7,8,9]
# cube=lambda y: y*y*y
# cube_list= list(map(cube,list2))
# print(cube_list)

### Reduce:
## Biggest Number Find
# import functools
# list3=[45,667,24,67,866,35,890,34]
# big=functools.reduce(lambda p,t: p if p>t else t, list3)
# print("Bigest Number in list:",big)

## Lowest number find:
# list4=[45,667,24,67,866,35,890,34]
# big1=functools.reduce(lambda b,c: b if b<c else c, list4)
# print("Lowest Number in list:",big1)
#### Oops Object Oriented Object

# class hira:
#     name=""
#     age=0
# #create hira1 ob
# hira1=hira()
# hira1.name="Hiraman"
# hira1.age=35
# #create appa1 another object:
# appa1=hira()
# appa1.name="Appa"
# appa1.age=34
# print(hira1.name, "is", hira1.age, "year old")
# print(f"{appa1.name} is {appa1.age} year old")

###Singal Inheritance:
# class A:
#     def add(self):
#         self.a=int(input("Enter first number : "))
#         self.b=int(input("Enter second number : "))

# class B(A):
#     def show(self):
#         print("The Multification is", self.a*self.b)
# obj=B()
# obj.add()
# obj.show()

#### Multilevel Inheritance:
# class D:
#     def add(self):
#         self.c=input("Enter first name : ")
#         self.d=input("Enter second name : ")

# class E(D):
#     def name1(self):
#         self.e=input("Enter City name : ")
#         self.f=input("Enter Chidren name : ")
        
# class F(E):
#     def show(self):
#         print("First Name is", self.c, self.d)
#         print(f"Children Name is {self.f} both are stay in {self.e} city") 

# obj=F()
# obj.add()
# obj.name1()
# obj.show()

#### Hidrid Inheritance:
# class father:
#     def add(self):
#         self.g=input("Enter Father name : ")
#         self.h=input("Enter Sarname name : ")

# class Chidren1(father):
#     def add1(self):
#         self.i=input("Enter First Children name : ")
# class Chidren2(father):
#     def add2(self):
#         self.j=input("Enter Second Children name : ")
# class family(Chidren1,Chidren2):
#     def show(self):
#         print(f"Family Name is {self.h}")
#         print(f"Family Head Name is {self.g} {self.h}")
#         print(f"Frist Chinldren Name is {self.i} {self.g} {self.h}")
#         print(f"Secound Chinldren Name is {self.j} {self.g} {self.h}")

# obj=family()
# obj.add()
# obj.add1()
# obj.add2()
# obj.show()

###hirchical Inheritance:
# class parent:
#     def company(self):
#         self.cname=input("Enter Company Name :")
#         self.address=input("Enter Company Address :")

# class employee(parent):
#     def getdata(self):
#         self.ename=input("Enter employee name : ")
#         self.eid=int(input("Enter Emp ID No : "))
#         print("Employee Name {}".format(self.ename))
#         print("Employee id is {}".format(self.eid))
# class show(parent):
#     def display(self):
#         print("Company Name is {}".format(self.cname))
#         print ("Adree of company is {}".format(self.address))

# s1=employee()
# s1.getdata()
# s=show()
# s.company()
# s.display()

##### Multiple inheritance:
class Collage:
    def getdata(self):
        self.no=int(input("Enter Registration number : "))
        self.name=input("Enter Collage Name : ")
        self.adress=input("Enter Adress : ")
    
    def display(self):
        print("Registration number of Collage {}".format(self.no))
        print("Collage Name is {}".format(self.name))
        print("Adress of Colleage {}".format(self.adress))

class Teacher():
    def info_tech(self):
        self.t_id=int(input("Enter id of Teacher: "))
        self.t_name=input("Enter Teacher Name : ")
        self.qulif=input("Enter qualification of Teacher : ")

    def show(self):
        print(" The id of teacher is {}".format(self.t_id))
        print(" The name of teacher is {}".format(self.t_name))
        print(" The qulification of teacher is {}".format(self.qulif))

class Student(Collage,Teacher):
    # Collage.getdata(Collage)
    # Collage.display(Collage)
    # Teacher.info_tech(Teacher)
    # Teacher.show(Teacher)
    def s_info(self):
        self.s_no=int(input("Enter Roll Number of Student : "))
        self.s_name=input("Enter Name of Student : ")
        self.s_add=input("Enter Address of Student : ")
        self.cr=input("Enter Cource of Student is : ")

    def s_dis(self):
        print("The Roll Number of student {}".format(self.s_no))
        print("The Name of student {}".format(self.s_name))
        print("The Address of student {}".format(self.s_add))
        print("The Course of student is {}".format(self.cr))

#create objetc of class student:
s1=Student()
s1.getdata()
s1.display()
s1.info_tech()
s1.show()
s1.s_info()
s1.s_dis()