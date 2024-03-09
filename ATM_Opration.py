### AMT Opration:
def displayMenu():
    print()
    print("HDFC Bank".center(20,'*'))
    print("1.Withdraw")
    print("2.Deposite")
    print("3.Check Balance")
    print("4.Check Pin")
    print("5.Exit")

## Withdraw:
def withdraw():
    global pin1, balance
    while True:
        print()
        user_pin = input("Enter Your Pin: ")
        if user_pin == pin1:
            while True:
                amount = int(input("Enter Amount to Withdraw: "))
                if amount > balance:
                    print(" Insufficeint Balance ! Balance:",balance)
                else:
                    balance-=amount
                    print("Withdraw Sucessfull ! Balance:",balance)
                    break
            break   
        else:
            print("Invalid Pin !!")

### Deposite:
def deposite():
    global balance
    print()
    while True:
        print()
        user_pin = input("Enter Your Pin: ")
        if user_pin == pin1:
            while True:
                amount = int(input("Enter Amount to Deposite: "))
                balance+=amount
                print("Deposite Sucessfull and Balance is:",balance)
                break
            break
        else:
            print("Invalid Pin !!")

### Balance Check:
def checkBalance():
    while True:
        user_pin = input("Enter Your Pin: ")
        if user_pin == pin1:
            print(" Name: ",name)
            print("Balance is:",balance)
            break
        else:
            print("Invalid Pin !!")

### Pin Change
def changePin():
    global pin1, balance
    while True:
        print()
        user_pin = input("Enter Your Pin: ")
        if user_pin == pin1:
            while True:
                pin1 = input("Enter New Pin: ")
                pin2 = input("Confrim Pin: ")
                if pin1==pin2:
                    print("Pin Updated Sucessfull")
                    break
                else:
                    print("Password not Matching")
            break
        else:
            print("Invalid Pin")

### Main Function To Call Other Functions:
def main():
    while True:
        displayMenu()
        ch = int(input("Enter Choice: "))

        if ch == 1:
            withdraw()
        elif ch==2:
            deposite()
        elif ch==3:
            checkBalance()
        elif ch==4:
            changePin()
        elif ch==5:
            break
        else:
            print("Wrong Input")
    print("Thank You !!!")

#### Main Code
### Taking Input
print()
name=input("Enter Your Good Name: ")
balance = int(input("Set Balance: "))
while True:
    print()
    pin1=input("Enter Pin: ")
    pin2=input("Confirm Pin: ")
    if pin1==pin2:
        print("Pin Set Sucessfull")
        break
    else:
        print("Password not matching")

### Calling the Main Function
main()
