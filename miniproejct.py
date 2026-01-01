def greet():
    name = (input("enter your name"))
    print("welcome to the mini project",name)

def oddeven():
    num = int(input("enter the number"))
    if num%2 ==0:
        print("the given number is even")
    else:
        print("the given number is odd")

def caluculator():
   sum1 = int(input("enter the first number"))
   sum2 = int(input("enter the second number"))
   print("addition",sum1 + sum2)

while True:
    print("\n........MENU........")
    print("1.Greet")
    print("2.Calculator")
    print("3.odd even")
    print("4.exit")
    choice = input("enter yout choice")
    if choice =="1":
     greet()
    elif choice=="2":
     caluculator()
    elif choice=="3":
        oddeven()
    elif choice=="4":
       print("thanks for choosing")
       break
    else:
        print("invalid choice")




    
