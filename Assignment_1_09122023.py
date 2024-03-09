#ASSIGNMEMT 1
# 1.Write a program to determine whether a person is eligible to vote.
age=int(input("Enter Age: "))
if (age >=18):
    print("Congratulations! You are eligible for Vote")
else:
    print("Sorry, You are not eligible for Vote")
    
#2.Program to print the largest of the three numbers.
num1=int(input("Enter the number1: "))
num2=int(input("Enter the number2: "))
num3=int(input("Enter the number3: "))
if (num1>num2) and (num1>num3):
    print(num1,"is largest number")
elif (num2>num1) and (num2>num3):
    print(num2,"is largest number")
elif (num3>num1) and (num3>num2):
    print(num3,"is largest number")
else:
    print("Please enter the correct Number")


#3.Program to print the largest of the two numbers.
num1=int(input("Enter the number1: "))
num2=int(input("Enter the number2: "))
if (num1>num2):
    print(num1,"is largest number")
elif (num2>num1):
    print(num2,"is largest number")
else:
    print("Please enter the correct Number")

#4.write a program to find whether the given number is even or odd.
num=int(input("Enter the Number: "))
if (num%2)==0:
     print("number is even")
else:
     print("number is odd")
     
# #5. write a program to enter any character. If the entered character is in lowercase then convert it into uppercase and if it is an uppercase character, then convert it into lowercase.
name=input("Enter your Name: ")
if "a" <=name<= "z":
    y=name.upper()
    print(y,"letter is converted into uppercase")
elif "A" <=name<= "Z":
    x=name.lower()
    print(x,"letter is converted into lowercase")
else:
    print("Please enter the proper character")

# #10.write a program to determine whether the character entered is a vowel or not.
txt=input("Enter the text: ")
vowel=['a','i','o','e','u','A','I','O','E','U']
if txt in vowel:
    print("Text is vowel")
else:
    print("Text is not vowel")
    
#9.program to test whether a number entered by the user is negative, positive, or equal to zero
num=int(input("Enter Number: "))
if num>0:
    print("Value is positive")
elif num==0:
    print("Value is zero")
else:
    print("Value is Negative")

#8.write a program to enter the marks of a student in four subjects. Then calculate the total and aggregate, and display the grade obtained by the student. If the student scores an aggregate greater than 75%, then the grade is Distinction. if aggregate is 60>=and <75, then the grade is first division. If aggregate is 50>=and<60, then the grade is Second division. If aggregate is 40>=and 50, then grade is third division. else the grade is fail.

eng=int(input("Enter marks of the English subject: "))
mth=int(input("Enter marks of the Math subject: "))
geo=int(input("Enter marks of the Geography subject: "))
sic=int(input("Enter marks of the Sicence subject: "))
sum=(eng+mth+geo+sic)
print(sum)
avg=(eng+mth+geo+sic)/4
print(avg)
if(avg>=75):
    print("Congratulations! Your grade is Distinction")
elif(avg>=60 and avg<75):
    print("Congratulations! Your grade is first division")
elif(avg>=50 and avg<60):
    print("Congratulations! Your grade is Second division")
elif(avg>=40 and avg<50):
    print("Congratulations! Your grade is Third division")
else:
    print("Sorry, you are fail, Better Luck Next Time")

#7. Program that prompts the user to enter a number and then print its interval
num1=int(input("Enter the Strat Number: "))
num2=int(input("Enter the End Number: "))
num3=int(input("Enter the Interval Number: "))
for num in range(num1,num2,num3):
    print(num)

#6. write a program to find whether a given year is a leap year or not.
year=int(input("Enter the Year: "))
if (year%4)==0:
    print(year,"This year is a leap year")
else:
    print(year,"This year is not leap year")