def addition():
    print("Enter two numbers you want to add")
    num1=int(input())
    print("Number1 = ",num1)
    num2=int(input())
    print("Number1 = ",num1)
    result=num1+num2
    print("The addition of enter numbers is ",result)
    
def subtraction():
    print("Enter two numbers you want to subtract")
    num1=int(input())
    print("Number1 = ",num1)
    num2=int(input())
    print("Number1 = ",num1)
    result=num1-num2
    print("The subtraction of enter numbers is ",result)
    
def multiplication():
    print("Enter two numbers you want to multiply")
    num1=int(input())
    print("Number1 = ",num1)
    num2=int(input())
    print("Number1 = ",num1)
    result=num1*num2
    print("The multiplication of enter numbers is ",result)
    
def division():
    print("Enter two numbers you want to divide")
    num1=int(input())
    print("Number1 = ",num1)
    num2=int(input())
    print("Number1 = ",num1)
    result=num1/num2
    print("The division of enter numbers is ",result)
    
def floor_division():
    print("Enter two numbers you want to divide")
    num1=int(input())
    print("Number1 = ",num1)
    num2=int(input())
    print("Number1 = ",num1)
    result=num1//num2
    print("The floor division of enter numbers is ",result)
    
def power():
    print("Enter the number you want to claculate the power of and the number to denote the power")
    num1=int(input())
    print("Number1 = ",num1)
    num2=int(input())
    print("Number1 = ",num1)
    result=num1**num2
    print("The power operation of enter numbers is ",result)
    
while(True):
    print("\nWANNA CALCULATE SOMETHING?")
    print("Enter your choice:")
    print("1.ADDITION")
    print("2.SUBTRACTION")
    print("3.MULTIPLICATION")
    print("4.DIVISION")
    print("5.FLOOR DIVISION")
    print("6.POWER")
    print("7.EXIT\n")
    choice=int(input())
    if choice == 1 :
        addition()
    elif choice == 2 :
        subtraction()
    elif choice == 3 :
        multiplication()
    elif choice == 4 :
        division()
    elif choice == 5 :
        floor_division()
    elif choice == 6 :
        power()
    elif choice == 7 :
        print("THANKS! HAVE A NICE DAY!")
        break
    else:
        print("OOPS! Invalid Choice!\nChoice must be from 1 to 7")
