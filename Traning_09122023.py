#Test 1#
# name=input("Enter your Name: ")
# div=input("Enter your div: ")
# eng=int(input("Enter your English Mark: "))
# math=int(input("Enter your Math Mark: "))
# sic=int(input("Enter your Science Mark: "))

# # print("--------------------Result------------------")
# # print("Name:",name, end="              ")
# # print("div:",div)
# # print("English:-",eng)
# # print("Math:-",math)
# # print("Science:-",sic)
# # print("--------------------------------------------")
# # sum=(eng+math+sic)
# # per=(sum/300)*100
# # print("Total=",sum, end="             " )
# # print("Percentage:",per,"%")

# #Str.format#
# # print('I am learing {} at "{}!"' .format('Python','Sumago Infotech'))

# # #Change Order#

# # print('I am learing {1} at "{0}!"' .format('Python','Sumago Infotech'))

# # Opretores#
# #Arithmatics Opretores#
# # prod1=int(input("Enter the Product1 Price: "))
# # prod2=int(input("Enter the Product2 Price: "))
# # add=(prod1+prod2)
# # sub=(prod1-prod2)
# # mul=(prod1*prod2)
# # div=(prod1/prod2)
# # divflo=(prod1//prod2)
# # mod=(prod1%prod2)
# # pow=(prod1**prod2)
# # print("Addition:",add)
# # print("Subtraction:",sub)
# # print("Multification:",mul)
# # print("Division:",div)
# # print("Division floor:",divflo)
# # print("Modulus:",mod)
# # print("Power:",pow)

# #Identity Operators#
# #Ex:1
# # aman="Hira"
# # suman=12
# # man="Hira"
# # print(aman is not suman)
# # print(aman is man)
# # #Ex:2
# # a=10
# # b=20
# # c=10
# # print(a is not b)
# # print(a is c)

# #Membership Operators:
# #Ex:1
# hira=["hiraman", 30, 40, 49, "sunil", 56, "appa"]
# a="appa"
# b=99
# c="suni"
# print(a not in hira)
# print(b in hira)
# print(c not in hira)
# print(a in hira)

#Ex:2
# hira=["hira", 70, 80, 99, "sunil", 78, "appa"]
# a="hira"
# b=99
# c="suni"
# if (a not in hira):
#     print("a is not in given list")
# else:
#     print("a is present in given list")

# if (b in hira):
#         print("b is present in given list")
# else:
#     print("b is not in given list")

#Even Odd find#
# pod=int(input("Enter the Product1 Price: "))
# if (pod%2)==0:
#     print("number is even")
# else:
#     print("number is odd")

## For loop
##For loop String#
# hira="I love India"
# for i in hira:
#     print(i)

# ## For loop list
# list=[1,5,"test", 78, "hret", 99]
# for i in list:
#     print(i)
    
## For Loop Range#
# for table in range(2,21,2):
#     print(table)

## While Loop#
# count=10
# while (count < 50):
#     count+=1
#     print("Hiraman")
#Create tabel useing for loop#
# hir=5
# for i in range(1,11):
#     print(hir, '*',i,'=',hir*i)

#In Loop "Break" "Continue" "Pass"
# vi="pandurang"
# for i in vi:
#     if i== "r":
#        break
#     print(i)
#Continue#
# vi="pandurang"
# for i in vi:
#     if i== "r":
#        continue
#     print(i)

#Pass#
# vi="pandurang"
# for i in vi:
#     if i== "r":
#        pass
#     print(i)